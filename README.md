# ✨ NovelCraft

[![Static Badge](https://img.shields.io/badge/Google-Gemini%201.0%20Pro-blue?logo=Google&logoColor=white&labelColor=black)](https://ai.google.dev/gemini-api)
[![Static Badge](https://img.shields.io/badge/HuggingFace-Diffusers%20MeinaPastel%20V6-pink?logo=HuggingFace&logoColor=white&labelColor=yellow)](https://huggingface.co/docs/diffusers/index)
[![Static Badge](https://img.shields.io/badge/Flask-API%20with%20Ngrok-red?logo=Flask&logoColor=black&labelColor=white)](https://ngrok.com/docs/using-ngrok-with/flask/)
[![Static Badge](https://img.shields.io/badge/Streamlit-Application-red?logo=Streamlit&logoColor=Red&labelColor=white)](https://docs.streamlit.io/)

- **What is NovelCraft?**

NovelCraft is an advanced AI tool designed to assist with your Lightnovel writing. With NovelCraft, you can easily generate new ideas, build characters, and outline your story structure. NovelCraft not only helps you plan your plot but also scores and provides detailed feedback on your content.

- **Key Features?**

A standout feature of NovelCraft is its ability to create cover art and illustrations based on your story content (currently in the experimental phase). NovelCraft uses large language models for NLP tasks and text-to-image technology to support you in both writing and illustrating.

- **Who Should Use NovelCraft?**

NovelCraft is aimed at novice and professional writers, students, and creative enthusiasts. It provides an overview and preliminary insight into developing a Lightnovel, helping you gain inspiration and motivation for your creative projects.

- **Demo**

Tiktok video: https://www.tiktok.com/@tml2504/video/7399913761013861640


# ❓ How to use

**Step 1:** Get the **Gemini API** and **Image Generator URL**

- Get **Gemini API** here: [Google AI Studio - Get API key](https://aistudio.google.com/app/apikey)

- Get **Image Generator URL**:

First, you need to run the ```flask-ngrok-api-diffusers.ipynb``` file with [Colab](https://colab.research.google.com/) or [Kaggle Notebook](https://www.kaggle.com/)

**NOTICE:** Replace the ```YOUR-NGROK-AUTH-TOKEN``` with your Ngrok token.

![Replace Ngrok Token](./img_app/How_to_use/ngrok_token.png)

Copy the URL ```https://XXXX-XX-XX-XXX-XXX.ngrok-free.app/generate_image```

![Image Generator URL](./img_app/How_to_use/image_generator_url.png)

**Step 2:** Run the app.py with Streamlit Application, enter the **Gemini API** and **Image Generator URL**
- Install Requirements

```
pip install -r requirements.txt
```

- Run app.py

```
streamlit run app.py
```

![Streamlit Application](./img_app/How_to_use/app.png)

- Enter the **Gemini API** and **Image Generator URL**

![Enter API and URL](./img_app/How_to_use/enter_api_url.png)

**Step 3:** Use the features

- **1. Chatbot**

![Chatbot Image](./img_app/How_to_use/chatbot_img.png)

- **2. Image Generator**

![Image Generator](./img_app/How_to_use/image_generator.png)

- **3. Lightnovel Generator**

Enter the input idea!

![Lightnovel Generator](./img_app/How_to_use/lightnovel_generator1.png)

Wait for the analysing and generating!

![Lightnovel Generator](./img_app/How_to_use/lightnovel_generator2.png)

Full results!

![Lightnovel Generator](./img_app/How_to_use/lightnovel_generator3.png)

AI Review!

![Lightnovel Generator](./img_app/How_to_use/lightnovel_generator4.png)

# 🏴󠁧󠁢󠁷󠁬󠁳󠁿 Terms of Use
- **Policy Purpose**

This policy aims to help users understand how NovelCraft operates. NovelCraft will not be held responsible for any copyright claims related to light novels, images, titles, etc. To use NovelCraft, users must have the API of Gemini as well as an API or URL from a related party that allows image generation based on tags.

- **User Rights and Obligations**

Users are allowed to freely use all features of NovelCraft to create light novels or images for personal needs (publication or entertainment, etc.). However, they may not use NovelCraft's name for publication or commercial purposes.

Users must ensure proper use of NovelCraft and not request light novels that are pornographic or contrary to general social morals.

- **Support and Contact**

Users can contact for support through the following information:

**Email:** trongvo250403@gmail.com

**Facebook:** [Trọng Võ](https://www.facebook.com/profile.php?id=100059263009845)

- **Policy Changes and Updates**

This policy may change as new features and operating methods are implemented. Users will be informed of policy changes.

- **Additional Terms and Conditions**

This policy is part of NovelCraft's service agreement.

Continued use of NovelCraft signifies that users agree to the terms and conditions in this policy.
