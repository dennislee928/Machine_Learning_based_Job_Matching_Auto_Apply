import openai

def generate_cover_letter(resume_text, job_description, openai_api_key):
    client = openai.OpenAI(api_key=openai_api_key)

    prompt = f"""你是一位專業的求職信撰寫專家。根據以下資訊撰寫一封求職信：
    履歷摘要：{resume_text}
    應徵職位描述：{job_description}
    
    請撰寫一封簡潔、專業且有針對性的求職信，凸顯我的經驗與該職位的匹配度。"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "你是一位專業的求職信撰寫專家，擅長幫助求職者撰寫有針對性的求職信。"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7,
        )
        cover_letter = response.choices[0].message.content.strip()
        return cover_letter
    except Exception as e:
        print(f"生成求職信時發生錯誤：{e}")
        return None

if __name__ == '__main__':
    # 使用範例
    resume_text = "擁有豐富人工智慧與軟體工程經驗的工程師。"
    job_description = "尋找熟悉人工智慧且有軟體開發經驗的工程師。"
    openai_api_key = "YOUR_OPENAI_API_KEY"  # 請替換為您的實際 API 金鑰
    cover_letter = generate_cover_letter(resume_text, job_description, openai_api_key)
    if cover_letter:
        print("求職信：\n", cover_letter)
    else:
        print("生成求職信失敗。")
