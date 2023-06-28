import random
import openai

class Chat:
    def __init__(self):
        openai.api_key = "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"
        modelprompt = "You are a mental health assistant/therapist. Ask open-ended questions, try to find problems, talk as if you are a human, and maintain a high variance and complexity to your speech and try to subtly mirror the mannerisms of the person you are talking to."
        self.model = "gpt-3.5-turbo"
        self.messages=[
            {"role": "system", "content": modelprompt}
        ]


    def generate_message(self, prompt):        
        to_send = self.messages.copy()
        to_send.append(
            {"role": "user", "content": "keep it short and clear, subtly figure out information about the person's life & mental health, maintain a high variance and complexity to your speech and subtly mirror speaking mannerisms. \nUser Message: \"" + prompt + "\""}
        )
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = to_send
        )
        
        bot_message = response['choices'][0]['message']['content']
        
        self.messages.extend(
            [{'role': 'user', 'content': prompt},
            {"role": "assistant", "content": bot_message}]
        )
        
        print(self.messages)
        return bot_message

    def get_hotlines(self):
        hotlines = {
            "Abortion": {
                "National Domestic Violence Hotline": "1-800-799-SAFE",
                "Post Abortion Counseling": "1-800-228-0332",
                "Post Abortion Project Rachel": "1-800-5WE-CARE",
                "National Abortion Federation Hotline": "1-800-772-9100",
                "National Office of Post Abortion Trauma": "1-800-593-2273"
            },
            "Abuse": {
                "National Sexual Assault Hotline": "1-800-656-HOPE (4673)",
                "Stop it Now!": "1-888-PREVENT",
                "United States Elder Abuse Hotline": "1-866-363-4276",
                "National Child Abuse Hotline": "1-800-4-A-CHILD (422-4453)",
                "Child Abuse Hotline / Dept of Social Services": "1-800-342-3720",
                "Child Abuse National Hotline": "1-800-25ABUSE",
                "Children in Immediate Danger": "1-800-THE-LOST",
                "Exploitation of Children": "1-800-843-5678",
                "National Association for Children of Alcoholics": "1-888-554-2627",
                "Missing Children Help Center": "1-800-872-5437"
            },
            "Addiction": {
                "Marijuana Anonymous": "1-800-766-6779",
                "Alcohol Treatment Referral Hotline (24 hours)": "1-800-252-6465",
                "Families Anonymous": "1-800-736-9805",
                "Cocaine Hotline (24 hours)": "1-800-262-2463",
                "Drug Abuse National Helpline": "1-800-662-4357",
                "National Association for Children of Alcoholics": "1-888-554-2627",
                "Ecstasy Addiction": "1-800-468-6933",
                "Alcoholics for Christ": "1-800-441-7877"
            },
            "Cancer": {
                "American Cancer Society": "1-800-227-2345",
                "National Cancer Institute": "1-800-422-6237"
            },
            "Christian Counseling": {
                "New Life Clinics": "1-800-NEW-LIFE",
                "National Prayer Line": "1-800-4-PRAYER",
                "Bethany Lifeline Pregnancy Hotline": "1-800-BETHANY",
                "Liberty Godparent Ministry": "1-800-368-3336",
                "Grace Help Line 24 Hour Christian Service": "1-800-982-8032",
                "The 700 Club Hotline": "1-800-759-0700",
                "Want to Know Jesus?": "1-800-NEED-HIM",
                "Biblical Help for Youth in Crisis": "1-800-HIT-HOME",
                "Rapha National Network": "1-800-383-HOPE",
                "Emerge Ministries": "330-867-5603",
                "Meier Clinics": "1-888-7-CLINIC or 1-888-725-4642",
                "Association of Christian Counselors": "1-800-526-8673",
                "Minirth Clinic": "1-888-MINIRTH (646-4784)",
                "Pine Rest": "1-800-678-5500",
                "Timberline Knolls": "1-877-257-9611",
                "Focus on the Family": "1-855-771-HELP (4357)"
            },
            "Chronic Illness/Pain": {
                "Rest Ministries": "1-888-751-REST (7378)",
                "Watchman Fellowship": "1-817-277-0023"
            },
            "Crisis #s (Teens Under 18)": {
                "Girls and Boys Town": "1-800-448-3000",
                "Hearing Impaired": "1-800-448-1833",
                "Youth Crisis Hotline": "1-800-448-4663",
                "Teen Hope Line": "1-800-394-HOPE"
            },
            "Crisis #s (Any Age)": {
                "United Way Crisis Helpline": "1-800-233-HELP",
                "Christian Oriented Hotline": "1-877-949-HELP",
                "Social Security Administration": "1-800-772-1213"
            },
            "Crisis Pregnancy Helpline": {
                "Crisis Pregnancy Hotline Number": "1-800-67-BABY-6",
                "Liberty Godparent Ministry": "1-800-368-3336"
            },
            "Domestic Violence": {
                "National Domestic Violence Hotline": "1-800-799-SAFE",
                "National Domestic Violence Hotline Spanish": "1-800-942-6908",
                "Battered Women and their Children": "1-800-603-HELP",
                "Elder Abuse Hotline": "1-800-252-8966",
                "RAINN": "1-800-656-HOPE (4673)"
            }
        }
        
        
        mymessages = self.messages.copy()
        if(mymessages[-1]["role"] == "assistant"):
            mymessages = mymessages[:-1]
        
        
        
        mymessages.append(
            {"role": "system", "content": f"using information from this discussion, choose 3 of the following hotline categories that would best suit the user {hotlines.keys()}\n\noutput with a 3 string long python list, with only given options. start your output with \"[\'\" and end it with \"\']\""}
        )
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = mymessages,
            max_tokens = 100
        )
        
        mymessages.pop()
        
        
        try:
            choosen_categories = eval(response['choices'][0]['message']['content'].strip().replace("```", "").replace("```", ""))
        except:
            return self.choose_hotline()
        
        print(f"{choosen_categories=}")
        
        hotlines_list = [hotline for category in choosen_categories for hotline in hotlines[category]]

        mymessages.append(
            {"role": "system", "content": f"using information from this discussion, choose 2 of the following hotlines that would best support the user {hotlines_list}\n\noutput with a 2 string long python list, with only given options. start your output with \"[\'\" and end it with \"\']\""}
        )
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = mymessages,
            max_tokens = 100
        )
        
        
        try:
            choosen_hotlines = eval(response['choices'][0]['message']['content'].strip().replace("```", "").replace("```", ""))
        except:
            return self.choose_hotline()
        
        print(f"{choosen_hotlines=}")
        
        decategorized = {}

        for category in hotlines.values():
            decategorized.update(category)
        
        
        toReturn = {choosen_hotlines[0]: decategorized[choosen_hotlines[0]], choosen_hotlines[1]: decategorized[choosen_hotlines[1]]}
        
        print(f"{toReturn=}")
        
        return toReturn
        
        
        
        
        
        
        
        
        
        
        
        