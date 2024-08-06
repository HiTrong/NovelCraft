# ====== Import Libraries ======
from prompt_templates import (
    get_idea_analysis_prompt,
    get_storyline_details_prompt,
    get_writing_part_prompt,
    get_summary_prompt,
    get_review_prompt,
    get_illustration_novel_prompt
)

from API_handle import get_gemini_response, get_picture_response
import streamlit as st
import pandas as pd
import re

# ====== Response Processing ======
def response_extract(response, lang):
    start = "[BẮT ĐẦU]" if lang == "Vietnamese" else "[START]"
    end = "[KẾT THÚC]" if lang == "Vietnamese" else "[END]"
    
    start_index = response.find(start)
    end_index = response.find(end)
    
    if start_index != -1 and end_index != -1:
        return response[start_index + len(start):end_index].strip()
    st.error("Something went wrong with the response! Please try again!")
    return response

def idea_extract(idea):
    pattern = re.compile(r'\[(\w+)\]:\s*(.*?)\s*(?=\[\w+\]:|$)', re.DOTALL)
    matches = pattern.findall(idea)
    
    result = {tag: value.strip() for tag, value in matches}
    try:
        del result["StoryLine"]
        del result["Chapter"]
    except:
        return {}
    return result

def split_by_tags(text):
    parts = re.split(r'(\[.*?\])', text)
    parts = [part.strip() for part in parts if part.strip()]
    
    # Tạo dictionary từ các phần tử đã tách
    result = {i: part for i, part in enumerate(parts)}
    
    return result

def get_review_df(review_str):
    def parse_review_str(review_str):
        review_str = review_str.replace('*','')
        sections = re.split(r'\n(?=\[)', review_str.strip())
        tags, scores, advice = [], [], []
        
        for section in sections:
            lines = section.split('\n', 1)
            if len(lines) < 2:
                continue
            
            tag_score_part = lines[0].strip()
            tag_match = re.match(r'\[(.*?)\]', tag_score_part)
            if tag_match:
                tag = tag_match.group(1).strip()
            else:
                tag = tag_score_part.strip()
            
            score_match = re.search(r'(\d+(\.\d+)?)\/\d+', tag_score_part)
            if score_match:
                score = score_match.group(1).strip()
            else:
                score = re.search(r'(\d+(\.\d+)?)', tag_score_part)
                if score:
                    score = score.group(1).strip()
                else:
                    score = ""
            
            advice_review_str = lines[1].strip()
            
            tags.append(tag)
            scores.append(score)
            advice.append(advice_review_str)
        
        return tags, scores, advice
    
    tags, scores, advice = parse_review_str(review_str)

    df = pd.DataFrame({
        "Tag": tags,
        "Score": scores,
        "Advice": advice
    })
    return df

# ====== Stage 1 ======
def analysis_idea(api_key:str, human_text:str, human_filetext:str, lang):
    prompt = get_idea_analysis_prompt(human_text, human_filetext, lang=lang)
    response = get_gemini_response(api_key, prompt, lambda: st.error("Please check your API and content moderation. Something went wrong!"))
    if response is None: return None
    response = response_extract(response, lang)
    return response

# ====== Stage 2 ======
def screenwriter(api_key:str, human_text:str, human_filetext:str, lang):
    prompt = get_storyline_details_prompt(human_text, human_filetext, lang=lang)
    response = get_gemini_response(api_key, prompt, lambda: st.error("Please check your API and content moderation. Something went wrong!"))
    if response is None: return None
    response = response_extract(response, lang)
    return response

def writing_screen(api_key:str, human_text:str, human_filetext:str, length_require:int, lang):
    prompt = get_writing_part_prompt(length_require, human_text, human_filetext, lang)
    response = get_gemini_response(api_key, prompt, lambda: st.error("Please check your API and content moderation. Something went wrong!"))
    if response is None: return None
    response = response_extract(response, lang)
    return response

# ====== Stage 3 ======
def illustrate(api_key:str, lightnovel:str, number_of_pictures:int, lang):
    prompt = get_illustration_novel_prompt(lightnovel, number_of_pictures, lang)
    response = get_gemini_response(api_key, prompt, lambda: st.error("Please check your API and content moderation. Something went wrong!"))
    if response is None: return None
    response = response_extract(response, lang)
    print(response)
    return response
    
def summary(api_key:str, lightnovel, lang):
    prompt = get_summary_prompt(lightnovel, lang)
    response = get_gemini_response(api_key, prompt, lambda: st.error("Please check your API and content moderation. Something went wrong!"))
    if response is None: return None
    response = response_extract(response, lang)
    return response

def review(api_key:str, lightnovel, pictures, lang):
    prompt_text = get_review_prompt(lightnovel, lang)
    if pictures is not None:
        prompt = [prompt_text] + pictures
    else:
        prompt = prompt_text
    response = get_gemini_response(api_key, prompt, lambda: st.error("Please check your API and content moderation. Something went wrong!"))
    if response is None: return None
    response = response_extract(response, lang)
    print(response)
    return response

def get_illustration(url: str, tag:str):
    try:
        img = get_picture_response(url, tag, lambda: st.error("Please check your API and content moderation. Something went wrong!"))
        return img
    except:
        return None