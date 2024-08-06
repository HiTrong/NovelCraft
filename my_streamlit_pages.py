# ====== Import Libraries ======
import streamlit as st
import yaml
import time
import json
import pandas as pd
import PIL.Image

from NovelGenerate import (
    # Stage 1
    analysis_idea,
    idea_extract,
    # Stage 2
    screenwriter,
    writing_screen,
    # Stage 3
    illustrate,
    summary,
    split_by_tags,
    get_illustration,
    review,
    get_review_df
    )

from Chatbot import (
    get_chatbot_response
)

from ImageGenerate import (
    image_generate
)

# ====== Languages Support ======
def get_language(lang="Vietnamese"):
    with open("language.yml","r",encoding='utf-8') as f:
        return yaml.safe_load(f)["vietnamese"] if lang == "Vietnamese" else yaml.safe_load(f)["english"]

# ====== Home Page ======
def HomePage(lang="Vietnamese"):
    language_dict = get_language(lang=lang)
    
    # Header
    st.title('✨ NovelCraft Introduction')
    
    # Introduction text
    st.write(language_dict['introduction'])    
    
# ====== Lightnovel Generator Page ======
def LightNovelGenerator(api_key:str, url:str, lang="Vietnamese"):
    language_dict = get_language(lang=lang)
    
    # Header
    st.title('🎬 Light Novel Generator')
    
    # Tab navigation
    chat_tab, novel_gen_tab, img_tag = st.tabs(["Chatbot","Novel Generate","Image Generate"])
    
    # Chat Tab
    with chat_tab:
        # Necessary session state
        if "history" not in st.session_state:
            st.session_state.history = []
                
        # Chat state
        chat_state = st.expander(language_dict["state_chat"])
                
        # Container
        container = st.container()
        
        # Show history
        with container:
            for message in st.session_state.history:
                st.chat_message(message["role"]).write(message["message"])
            
        if human_input := st.chat_input(language_dict["chat_label"]):
            # Add message to history
            st.session_state.history.append({
                "role": "user",
                "message": human_input
            })
            
            with container:
                st.chat_message("user").write(human_input)
                
            # Get response and add to history
            with chat_state:
                start = time.time()
                response = get_chatbot_response(api_key, human_input, lang)
                if response != "Please try again later!":
                    st.write(f"Complete in {time.time() - start} seconds")
                    
            st.session_state.history.append({
                "role": "ai",
                "message": response
            })
            
            with container:
                st.chat_message("ai").write(response)
    
    # Novel Generate Tab    
    with novel_gen_tab:
        # Number of words to generate
        number_of_words = st.slider(
            language_dict["number_of_words"], 
            min_value=1000, 
            max_value=10000, 
            step=100, 
            value=1000,
            key = "number_of_words"
        )
        
        # Checkboxes for Illustration, Review, Get Summary File, 
        checkbox1, checkbox2, cost_show = st.columns(3)
        with checkbox1:
            review_checkbox = st.checkbox(language_dict["review"], key="review")
            get_summary_file = st.checkbox(language_dict["get_summary_file"], key="getsummaryfile")
            illustration = st.checkbox(language_dict["illustration"], key="illustration")

        number_of_illustration = 0
        with checkbox2:
            if illustration:
                number_of_illustration = st.slider(
                    language_dict["number_of_illustration"], 
                    min_value=1, 
                    max_value=5, 
                    step=1, 
                    value=2,
                    key = "number_of_illustration"
                )
        
        # Calculate costs
        costs = 3 + sum([review_checkbox, get_summary_file]) + number_of_illustration
        # Show costs
        with cost_show:
            st.markdown("<h3 style='text-align: center;'>{} requests</h3>".format(costs), unsafe_allow_html=True)
        
        # File Uploader
        uploaded_file = st.file_uploader("Upload Analysis File", type="json")
        
        try:
            filetext = uploaded_file.read().decode("utf-8") if uploaded_file is not None else None
            if uploaded_file is not None:
                analysis_file = json.loads(filetext)
                required_keys = ["Name", "Characters", "Background", "Categories", "Main Story" ,"Summary"]
                missing_keys = [key for key in required_keys if key not in analysis_file]
        
                if missing_keys:
                    raise KeyError(f"JSON missing: {', '.join(missing_keys)}")
                    return
        except json.JSONDecodeError as e:
            st.error(f"JSON error: {e}")
            return
        except Exception as e:
            st.error(f"Error: {e}")
            return
        
        # input
        if "send_input" not in st.session_state:
            st.session_state.send_input = False
            
        def clear_input():
            st.session_state.user_idea = st.session_state.user_input
            st.session_state.user_input = ""
        
        def update_send_input_state():
            st.session_state.send_input = True
            clear_input()
        
        novel_input = st.text_area(language_dict['novel_input'],height=200,key="user_input",on_change=update_send_input_state)
        
        if st.session_state.send_input:
            start = time.time()
            st.session_state.send_input = False
            
            if api_key == "" or (illustration and url == ""):
                st.warning(language_dict["api_key_blank"])
                return

            
            # 3 Stages 
            stage1, stage2, stage3 = st.columns(3)
            with stage1:
                stage1_status = st.status(label=language_dict['stage1_label'],expanded=True, state="running")
            with stage2:
                stage2_status = st.status(label=language_dict['stage2_label'],expanded=False, state="running")
            with stage3:
                stage3_status = st.status(label=language_dict['stage3_label'],expanded=False, state="running")
                
            while True:
                with stage1_status as status:
                    st.write(language_dict["stage1"]["step1"])
                    time.sleep(0.5)
                    st.write(language_dict["stage1"]["step2"])
                    
                    idea = analysis_idea(api_key, st.session_state.user_idea, filetext, lang)
                    if idea is None:
                        status.update(state="error", expanded=True)
                        stage2_status.update(state="error", expanded=False)
                        stage3_status.update(state="error", expanded=False)
                        break
                    else: 
                        st.write(language_dict["stage1"]["step3"])
                        time.sleep(0.5)
                        idea_dict = idea_extract(idea)
                        status.update(state="complete", expanded=False)
                        
                # Show Information
                st.write("### Name: " + idea_dict["Name"]) if "Name" in idea_dict else st.write("#### Name: Unknown")
                with st.expander("Details"):
                    st.write("##### Categories: \n" + idea_dict["Categories"]) if "Categories" in idea_dict else st.write("##### Categories: Unknown")
                    st.write("##### Background: \n" + idea_dict["Background"]) if "Background" in idea_dict else st.write("##### Background: Unknown")
                    st.write("##### Characters: \n" + idea_dict["Characters"]) if "Characters" in idea_dict else st.write("##### Characters: Unknown")
                

                with stage2_status as status:
                    status.update(expanded=True)
                    st.write(language_dict["stage2"]["step1"])
                    screen = screenwriter(api_key, idea, filetext, lang)
                    if screen == None:
                        stage2_status.update(state="error", expanded=True)
                        stage3_status.update(state="error", expanded=False)
                        st.warning("Please try again!")
                        return
                    st.write(language_dict["stage2"]["step2"])
                    lightnovel = writing_screen(api_key, screen, filetext, number_of_words/2, lang)
                    if lightnovel is None:
                        stage2_status.update(state="error", expanded=True)
                        stage3_status.update(state="error", expanded=False)
                        st.warning("Please try again!")
                        return
                    else: 
                        st.write(language_dict["stage2"]["step3"])
                        time.sleep(0.5)
                        status.update(state="complete", expanded=False)

                with stage3_status as status:
                    status.update(expanded=True)
                    st.write(language_dict["stage3"]["step1"])
                    if get_summary_file:
                        st.write(language_dict["stage3"]["step2"])
                        lightnovel_summary = summary(api_key, lightnovel, lang)
                        if lightnovel_summary == None:
                            stage3_status.update(state="error", expanded=True)
                            st.warning("Please try again!")
                            return
                        idea_dict["Summary"] = [lightnovel_summary]
                        if uploaded_file is None:
                            json_str = json.dumps(idea_dict, ensure_ascii=False, indent=4)
                        else:
                            analysis_file["Summary"].append(lightnovel_summary)
                            json_str = json.dumps(analysis_file, ensure_ascii=False, indent=4)
                        json_bytes = json_str.encode('utf-8')
                        st.download_button(
                            label="Download",
                            data=json_bytes,
                            file_name="analysis_file.json",
                            mime="application/json"
                        )
                        
                    if illustration:
                        if url is None or url == "":
                            st.warning("Missing URL parameter!")
                            return
                        else:
                            st.write(language_dict["stage3"]["step3"])
                            lightnovel_with_illustration = illustrate(api_key, lightnovel, number_of_illustration, lang)
                            if lightnovel_with_illustration == None:
                                stage3_status.update(state="error", expanded=True)
                                st.warning("Please try again!")
                                return
                            lightnovel_dict = split_by_tags(lightnovel_with_illustration)
                            lightnovel_show = []
                            try:
                                for key in lightnovel_dict:
                                    s = lightnovel_dict[key]
                                    if s.startswith("[") and s.endswith("]"):
                                        tag = s.replace("[PictureTag: ", "").replace("]", "")
                                        lightnovel_show.append(get_illustration(url, tag))
                                    else:
                                        lightnovel_show.append(s)
                            except:
                                st.warning("Please check your Image Generator URL! Something went wrong!")
                                return
                            
                            if review_checkbox:
                                st.write(language_dict["stage3"]["step4"])
                                AI_review = review(api_key, lightnovel, [img for img in lightnovel_show if str(type(img)) != "<class 'str'>"], lang)
                                if AI_review == None:
                                    stage3_status.update(state="error", expanded=True)
                                    st.warning("Please try again!")
                                    return
                    else:
                        lightnovel_show = [lightnovel]
                        if review_checkbox:
                            st.write(language_dict["stage3"]["step4"])
                            AI_review = review(api_key, lightnovel, None, lang)
                            if AI_review == None:
                                stage3_status.update(state="error", expanded=True)
                                st.warning("Please try again!")
                                return
                                
                    st.write(language_dict["stage3"]["step5"])
                    status.update(state="complete", expanded=False)
                          
                # Show Lightnovel
                # Content
                for content in lightnovel_show:
                    if str(type(content)) == "<class 'str'>":
                        st.write(content)
                    else:
                        st.image(content, caption="Illustration", use_column_width=True)
                                
                # Show review
                if review_checkbox:
                    review_df = get_review_df(AI_review)
                    st.write("#### AI Review")
                    st.table(review_df)
                    
                # Show time
                st.write(f"#### Total time: {time.time() - start}s")
                break

    # Image Generate Tab
    with img_tag:        
        # Image History Session
        if "img_history" not in st.session_state:
            st.session_state.img_history = []
            
        if human_tag := st.chat_input(language_dict["tag_label"]):
            start = time.time()
            img_gen = image_generate(url, human_tag)
            # Add to history
            st.session_state.img_history.append({
                "tag": human_tag,
                "img": img_gen,
                "time": (time.time()-start)
            })
            
        # Container
        with st.container():
            for img_message in st.session_state.img_history:
                with st.expander("TAG: " + img_message["tag"] + " - Time: " + str(round(img_message["time"], 4)), expanded=False):
                    st.image(img_message["img"], "Image Generated")
        
        
# ====== Terms of Use ======
def TermsOfUse(lang="Vietnamese"):
    language_dict = get_language(lang=lang)
    
    # Header
    st.title("🏴󠁧󠁢󠁷󠁬󠁳󠁿 Terms of Use")
    
    # Content
    st.write(language_dict["terms"])