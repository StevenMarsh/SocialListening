from watson_developer_cloud import ToneAnalyzerV3
import simplejson as json

tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    iam_apikey='oMsOr-VXaaNU9V5D9Pg0AXrC99jK1gJ4t1DGtgjfuKu7',
    url='https://gateway.watsonplatform.net/tone-analyzer/api'
)

text='Wonderful!!! 3 year old missing 3 days is found. No sign of any abduction. He is alert, happy to be back with his family, and asking to watch Netflix, so he seems to be out of the woods every which way.'
'''text = 'Team, I know that times are tough! Product '\
    'sales have been disappointing for the past three '\
    'quarters. We have a competitive product, but we '\
    'need to do a better job of selling it!
    '''

tone_analysis = tone_analyzer.tone(
    {'text': text},
    'application/json'
).get_result()
print(json.dumps(tone_analysis, indent=2))

#REMEMBER TO GO TO IAMGENERATOR TO GET A NEW ACCESS TOKEN AND REFRESH TOKEN#################

#"access_token":"eyJraWQiOiIyMDE3MTAzMC0wMDowMDowMCIsImFsZyI6IlJTMjU2In0.eyJpYW1faWQiOiJpYW0tU2VydmljZUlkLTE0MDNlY2ZlLWYyYTMtNGZiMy04OThjLTdmYjlkMTkwZGE4NiIsImlkIjoiaWFtLVNlcnZpY2VJZC0xNDAzZWNmZS1mMmEzLTRmYjMtODk4Yy03ZmI5ZDE5MGRhODYiLCJyZWFsbWlkIjoiaWFtIiwiaWRlbnRpZmllciI6IlNlcnZpY2VJZC0xNDAzZWNmZS1mMmEzLTRmYjMtODk4Yy03ZmI5ZDE5MGRhODYiLCJzdWIiOiJTZXJ2aWNlSWQtMTQwM2VjZmUtZjJhMy00ZmIzLTg5OGMtN2ZiOWQxOTBkYTg2Iiwic3ViX3R5cGUiOiJTZXJ2aWNlSWQiLCJ1bmlxdWVfaW5zdGFuY2VfY3JucyI6WyJjcm46djE6Ymx1ZW1peDpwdWJsaWM6dG9uZS1hbmFseXplcjp1cy1zb3V0aDphL2I1ZmNmMDE3NjhhNjQ5MDY4MTUxNDc3ZTlmZjNiZTI3OjYwODU1MDU0LTAxNzItNGM5ZC04NzVmLTRiYjYwNDQyMTY0MTo6Il0sImFjY291bnQiOnsidmFsaWQiOnRydWUsImJzcyI6ImI1ZmNmMDE3NjhhNjQ5MDY4MTUxNDc3ZTlmZjNiZTI3In0sImlhdCI6MTU0ODU2OTc5NiwiZXhwIjoxNTQ4NTczMzk2LCJpc3MiOiJodHRwczovL2lhbS5jbG91ZC5pYm0uY29tL2lkZW50aXR5IiwiZ3JhbnRfdHlwZSI6InVybjppYm06cGFyYW1zOm9hdXRoOmdyYW50LXR5cGU6YXBpa2V5Iiwic2NvcGUiOiJpYm0gb3BlbmlkIiwiY2xpZW50X2lkIjoiZGVmYXVsdCIsImFjciI6MSwiYW1yIjpbInB3ZCJdfQ.hbQHpfJbGrxG0JEovYHK8EAeGRqO4Mo79GHsrZVCldiplrzB8NqbLo4elg-JHBF_jCj9JhvfJn0skFfiGmaOWe6BkxbXBdkIsfbXgenCrkOi2tdPk_9uF6cm8szQwrprfrPKI_2oATM6d605U-Jo78vV_1NmwCfFfJjJNrN4cL_ZYxWtDgFP1icZIhjx74jAsLVsDGRwDZLV79F3YFkZAUnRh244oP987gp0OaG6gZRT0yEUZpK6R1LHofTpUNmifn3Yk7Wqv-gv1KQhOTGnnsVn4WVu_wmhJWzN0Pm46aKXE5y1rt3YgktOXPpoqYXwXkTrjvMDumIuPopeAEtnBA"

#"refresh_token":"J1BnE_lJLsieUey2GkQSMaODZmfkgL0ju6tJmwTUMS_68Vkj7DvBF7SrsW5HsASbSpMOCww8T6dS8cqcAKB_1OylHJvu9nbfpXl2qQ-K8jMKvLY2b_T1LhGEiRjtt8VXPR_4AML6nQfb0JqBSp3H6hXbSkFBZ0w6KyUofWvCdp2Wnc1zw_l9e59Rn8NR--dbSFnqSEXEYnM5c6ehiZ_7wneRqqrW3A1dVWwr5mvw1xh0ZtnZlT-7MmPKx01PDb9QHzdGFbUmO0bi16C3ll2OsRv09Qt2m7wFT2z2hFvleG9Qo59MI8M9LDix5rnEWbTVvo2x2MR8k2_WVEcrDchQy4b4Dup3-F_B0yJRBe9xVbqtdMW4ngqBbgSzffNeXcUS-n0ToLBjnVtJ6ooZBK8S8Xso_-N6IX8Lv7EYMDAMuZLtTEScPjPy3-Tww8xphqZuhpoCkSBBLvxc27KFqr-piDFx3QJ8_UHyx9JJswi27x0C1wJbk_drM6gLVqihtygfFNqnHkMq1mMHdQJMgubQM1YKElWUZwgFEYNF_x-6sC3vz9qpfcNA1QH_9eRlD22sSV0ntC3fl-_zwRSuquZsj_WOLUlXRJHfKOsmvDNdG-lpDSgNHJf8Tbv8DsjMhnvtX0dQGN3grEVNqrcI6vJRxF5FXuLLBiw2yES_d95Z7W-foiGhfCGgAS9vHvEkTgi_Xg-dLlAAIaWhpv_dfyPs83J3cjHJp9bfvDzNB4zGixCAqUpJazaswoxNvtSZuLOvzU6G1g431nnhgEjyefRuC_Qq6g5bk_PRYntc9avHuutSB3ta5RvF-cYi-Evk090bCGxTvsyTc_Av8ZfQl1zxARHVLKjl1qPJYBL_aDWrHLahf2258QedNj3T0mmUDNzm3q_SG0vNaCtk_CYBMSq2qVtJVyxGiJmzTDPBSiYGrIaf9aVRs4OIytBJjCio6Lgq-FvmSq0twwWaN-D3rpYEFGUitxsBEkEy12K4840ntYMI2w"












'''import requests
import json

def analyze_tone(text):
    username = 'willynee1995@gmail.com'
    password = 'Baxter123!'
    watsonUrl = 'https://gateway.watsonplatform.net/tone-analyzer-beta/api/v3/tone?version=2016-05-18'
    headers = {"content-type": "text/plain"}
    data = text
    try:
        r = requests.post(watsonUrl, auth=(username,password),headers = headers,
         data=data)
        return r.text
    except:
        return False


def welcome():
    message = "Welcome to the IBM Watson Tone Analyzer\n"
    print(message + "-" * len(message) + "\n")
    message = "How it works"
    print(message)
    message = "Perhaps a bit too aggressive in your emails? Are your blog posts a little too friendly? Tone Analyzer might be able to help. The service uses linguistic analysis to detect and interpret emotional, social, and writing cues found in text."
    print(message)
    print()
    print("Have fun!\n")

def display_results(data):
    data = json.loads(str(data))
    print(data)
    for i in data['document_tone']['tone_categories']:
        print(i['category_name'])
        print("-" * len(i['category_name']))
        for j in i['tones']:
            print(j['tone_name'].ljust(20),(str(round(j['score'] * 100,1)) + "%").rjust(10))
        print()
    print()


 
def main():
    welcome()
     
    data = input("Enter some text to be analyzed for tone analysis by IBM Watson (Q to quit):\n")
    if len(data) >= 1:
        if data == 'q'.lower():
            exit
        results = analyze_tone(data)
        if results != False:
            display_results(results)
            exit
        else:
            print("Something went wrong")
 
main()'''
