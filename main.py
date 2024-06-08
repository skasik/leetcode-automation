import botAssistantModule as bot
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from botAssistantModule import Devices, Browsers
import os
from selenium.webdriver.common.alert import Alert 
import pyperclip
import requests
import json
# username = os.getenv("USERNAME")
# password = os.getenv("PASSWORD")

model = None


def readJson():
    try:
        with open("temp.json", "r") as file:
            data = json.load(file)
        return data["last_tried"]
    except:
        link = "https://leetcode.com/problems/two-sum/description/"
        writeJson(link)
        return link

def writeJson(data):
    with open("temp.json", "w") as file:
        json.dump({"last_tried":data}, file)


def login():
    model.goToLink("https://leetcode.com/")
    
    model.browser.add_cookie({"name":"1P_JAR","value":"2024-06-06-08"})
    model.browser.add_cookie({"name":"87b5a3c3f1a55520_gr_cs1","value":"autoleet"})
    model.browser.add_cookie({"name":"87b5a3c3f1a55520_gr_last_sent_cs1","value":"autoleet"})
    model.browser.add_cookie({"name":"87b5a3c3f1a55520_gr_last_sent_sid_with_cs1","value":"0d190c5f-33ed-40c2-af89-fa057bf979ac"})
    model.browser.add_cookie({"name":"87b5a3c3f1a55520_gr_session_id","value":"0d190c5f-33ed-40c2-af89-fa057bf979ac"})
    model.browser.add_cookie({"name":"87b5a3c3f1a55520_gr_session_id_sent_vst","value":"0d190c5f-33ed-40c2-af89-fa057bf979ac"})
    model.browser.add_cookie({"name":"AEC","value":"AQTF6HybKjXTh8_phzqgM8iTuqZHngjaJY9skOzyi8ZXlFt5kAgqbKziMw"})
    model.browser.add_cookie({"name":"INGRESSCOOKIE","value":"3014e52e6aa8a03befb9068ad0ed1bcd|8e0876c7c1464cc0ac96bc2edceabd27"})
    model.browser.add_cookie({"name":"LEETCODE_SESSION","value":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X3ZlcmlmaWVkX2VtYWlsIjpudWxsLCJhY2NvdW50X3VzZXIiOiI4MzV2cCIsIl9hdXRoX3VzZXJfaWQiOiIxMzU4NDUxNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImYxOGMxOGIzNjcwZGVmZWIxYzY0NTY4NTA3NGVkYThkODI5NDNhODY1Y2Q0MjY3MmUzZmY0ZGM0MTIwZGI3MGQiLCJpZCI6MTM1ODQ1MTcsImVtYWlsIjoidGluaWVzdF9jbGF3XzA4QGljbG91ZC5jb20iLCJ1c2VybmFtZSI6ImF1dG9sZWV0IiwidXNlcl9zbHVnIjoiYXV0b2xlZXQiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvZGVmYXVsdF9hdmF0YXIuanBnIiwicmVmcmVzaGVkX2F0IjoxNzE3NjY5ODg3LCJpcCI6IjEwMy4xOTYuMjE3LjIzMyIsImlkZW50aXR5IjoiODM4MWMwNDhhOWQ3MDIzMGFmMTNhMTJhNzY2NjNkYzQiLCJzZXNzaW9uX2lkIjo2MzAxNjE2MX0.dVs9mGtlAhebUUMjTCaBFl5H8rl4WN8EsgTDe1lURFo"})
    model.browser.add_cookie({"name":"NID","value":"514=bu4bzWBi944gSwDTnHRnQIYXBsFSt57Dpgsfq4DMAA4XSdbbq7C-qDQYGpRftPu9u6JhKv_mU8Dh_6tmE4Ji6CPnJOqzGZsXfwUo3oaAp6dRV1VvWOBENBnqM0u23rFsS5QHQlCyEloLJAXgPwopmDIciXK9YXtzv_-PV19FreFJX5qDr6d6qMZpuGyg0Qh255dTvYkY_g"})
    model.browser.add_cookie({"name":"__cf_bm","value":"z.XyPT_rystsya6W6qcF.l2o6UYPWOd_Mu_TZV0e1T8-1717671160-1.0.1.1-0XECGy1UtE9on69_vFWshpYmUv6xgup1QOpLBNpnwKl52NbKg5jfiSmTx7hmjH3ehrfYSPlpXNBS3ou50taMJg"})
    model.browser.add_cookie({"name":"_dd_s","value":"rum=0&expire=1717672061819"})
    model.browser.add_cookie({"name":"_ga","value":"GA1.2.1148708977.1717671161"})
    model.browser.add_cookie({"name":"_ga_CDRWKZTDEX","value":"GS1.1.1717671160.1.0.1717671160.60.0.0"})
    model.browser.add_cookie({"name":"_gat","value":"1"})
    model.browser.add_cookie({"name":"_gid","value":"GA1.2.1087989237.1717671161"})
    model.browser.add_cookie({"name":"cf_chl_rc_m","value":"1"})
    model.browser.add_cookie({
        "name": "csrftoken",
        "value": "8Lc9Mid8VWVfZmkQiJbmrqi3ERsxvV63DMDYd9JWquISbec1766OzLhbCJ3EFGYO",
    })
    model.browser.add_cookie({"name":"gr_user_id","value":"a39e72ea-2038-43d1-90dc-06e0e259c05a"})



def nextQues():
    # model.browser.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[3]/nav/div/div/div[1]/div/a[2]').click()
    # href = model.browser.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[3]/nav/div/div/div[1]/div/a[2]').get_attribute("href")
    # model.goToLink(href)
    # model.browser.execute_script('document.querySelector("#__next > div.flex.h-\\[100vh\\].min-w-\\[360px\\].flex-col.overflow-x-auto.text-label-1.dark\\:text-dark-label-1 > div > div > div.relative > nav > div > div > div:nth-child(1) > div > a:nth-child(5)").click()')
    model.browser.execute_script("document.querySelectorAll('a.group')[1].click();")
    print(model.browser.find_elements(By.CSS_SELECTOR, 'a.group')[1].get_attribute("href"))
    model.sleepRandom(8,10)

def hitAPI():
    link = "https://leetcode.com/problems/two-sum/submit/"
    headers = {
        "authority": "leetcode.com",
        "method": "POST",
        "path": "/problems/two-sum/interpret_solution/",
        "scheme": "https",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "content-length": "0",
        "content-type": "application/json",
        "set-cookie" : """LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X3ZlcmlmaWVkX2VtYWlsIjpudWxsLCJhY2NvdW50X3VzZXIiOiI4MzV2cCIsIl9hdXRoX3VzZXJfaWQiOiIxMzU4NDUxNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImYxOGMxOGIzNjcwZGVmZWIxYzY0NTY4NTA3NGVkYThkODI5NDNhODY1Y2Q0MjY3MmUzZmY0ZGM0MTIwZGI3MGQiLCJpZCI6MTM1ODQ1MTcsImVtYWlsIjoidGluaWVzdF9jbGF3XzA4QGljbG91ZC5jb20iLCJ1c2VybmFtZSI6ImF1dG9sZWV0IiwidXNlcl9zbHVnIjoiYXV0b2xlZXQiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvZGVmYXVsdF9hdmF0YXIuanBnIiwicmVmcmVzaGVkX2F0IjoxNzE3NjY5ODg3LCJpcCI6IjEwMy4xOTYuMjE3LjIzMyIsImlkZW50aXR5IjoiODM4MWMwNDhhOWQ3MDIzMGFmMTNhMTJhNzY2NjNkYzQiLCJzZXNzaW9uX2lkIjo2MzAxNjE2MX0.dVs9mGtlAhebUUMjTCaBFl5H8rl4WN8EsgTDe1lURFo; Domain=.leetcode.com; expires=Thu, 20 Jun 2024 12:36:45 GMT; HttpOnly; Max-Age=1209600; Path=/; SameSite=Lax; Secure""",
        # "Strict-Transport-Security": "max-age=31536000; includeSubDomains; preload",
        # "Vary":"Cookie",
        # "X-Content-Type-Options":"nosniff",
        # "X-Frame-Options":"DENY",
    }
    payload = {"lang":"cpp","question_id":"1","typed_code":"#include <unordered_map>\n#include <vector>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<int> twoSum(vector<int>& nums, int target) {\n        unordered_map<int, int> map;\n        std::vector<int> indices;\n\n        // save items with their index\n        for (int i = 0; i < nums.size(); i++) {\n            map.insert(std::make_pair(nums[i], i));\n        }\n\n        for (int i = 0; i < nums.size(); i++) {\n            int missing = target - nums[i];\n\n            auto item = map.find(missing);\n            // found, and don't use same number!\n            if (item != map.end() && i != item->second){\n                indices.push_back(i);\n                indices.push_back(item->second);\n                return indices;\n            }\n        }\n        return indices;\n    }\n};","data_input":"[2,7,11,15]\n9\n[3,2,4]\n6\n[3,3]\n6"}
    response = requests.post(link, headers=headers, data=payload)
    print(response.text)


if __name__ == "__main__":
    model = bot.botAssistant()
    model.sleepRandom_minTime = 5
    model.sleepRandom_maxTime = 10
    model.setUserAgent(Devices.IPHONE)
    model.openBrowser(browser=Browsers.CHROME)
    
    login()

    # model.goToLink("https://leetcode.com/problems/two-sum/description/")
    questions = json.load(open("leetcodeAutomation.py/all_problems.json"))["data"]["problemsetQuestionList"]["questions"]
    # model.goToLink(readJson())


    for ques in questions:
        try:
            # if "/problems/" in model.browser.current_url and "/submissions/" not in model.browser.current_url and "/solutions/" not in model.browser.current_url:
            #     writeJson(model.browser.current_url)
            model.goToLink("https://leetcode.com/problems/"+ques["titleSlug"]+"/description/")
            model.browser.find_element(By.ID,"solutions_tab").click()
            model.sleepRandom(2,5)
            for el in model.browser.find_elements(By.CSS_SELECTOR , 'div.flex > div.flex > span'):
                if el.text == "C++":
                    el.click()
                    break
            model.sleepRandom(5,8)
            # model.browser.find_elements(By.CSS_SELECTOR , 'div.relative > div.relative > div.flex > div.group:nth-child(1)')[2].click()
            model.browser.execute_script("document.querySelectorAll('div.relative > div.relative > div.flex > div.group:nth-child(1)')[2].click()")
            model.sleepRandom(5,8)
            # model.browser.execute_script("document.querySelector('code.language-cpp').parentElement.parentElement.childNodes[1].childNodes[0].childNodes[0].scrollIntoView()")
            # model.browser.execute_script("document.querySelector('code.language-cpp').parentElement.parentElement.childNodes[1].childNodes[0].childNodes[0].click()")
            temp = model.browser.find_elements(By.CSS_SELECTOR, 'code.language-cpp')[-1]
            code = ""
            for spanMain in temp.find_elements(By.CSS_SELECTOR, "span"):
                for span in spanMain.find_elements(By.CSS_SELECTOR, "span"):
                    code += span.text
                code += "\n"
            print(code)

            model.sleepRandom(2,3)
            try:
                for i in range(200): 
                    model.typeKeys(Keys.DELETE,  model.browser.find_element(By.XPATH, '//*[@id="editor"]/div[2]/div[1]/div/div/div[1]/textarea'), 0.02)
            except Exception as e:
                print("Error"+str(e))

            # model.browser.find_element(By.XPATH, '//*[@id="editor"]/div[2]/div[1]/div/div/div[1]/textarea').send_keys(code)
            for i in range(0, len(code)):
                if code[i] == '\n':
                    if i != len(code)-1 and code[i+1] != '\n':
                        model.typeKeys(Keys.ENTER, model.browser.find_element(By.XPATH, '//*[@id="editor"]/div[2]/div[1]/div/div/div[1]/textarea'), 0.01)
                else:
                    model.typeKeys(code[i], model.browser.find_element(By.XPATH, '//*[@id="editor"]/div[2]/div[1]/div/div/div[1]/textarea'), 0.01)
                    model.typeKeys(Keys.DELETE, model.browser.find_element(By.XPATH, '//*[@id="editor"]/div[2]/div[1]/div/div/div[1]/textarea'), 0.01)

            model.browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[4]/div/div/div[8]/div/div[1]/div[2]/button[1]").click()
            model.sleepRandom(15,20)
        except Exception as e:
            print("Error"+str(e))
            model.goToLink(model.browser.current_url)
            continue

        # try:
        #     for i in range(500): 
        #         model.typeKeys(Keys.DELETE,  model.browser.find_element(By.XPATH, '//*[@id="editor"]/div[2]/div[1]/div/div/div[1]/textarea'), 0.02)
        # except Exception as e:
        #     print("Error"+str(e))

        

        model.browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[3]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div[3]/div[3]/div/button").click()
        model.sleepRandom(10,15)
        # nextQues()


    # while True:
    #     nextQues()
    #     print("Next Question")
    #     model.sleepRandom(4,5)

