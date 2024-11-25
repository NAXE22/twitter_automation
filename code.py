from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



#define a class with methods to login, like tweet etc

class TwitterBot:
    def __init__(self,user_name,password) -> None:
        self.user_name=user_name
        self.password=password
       
    def setup_driver(self):
         options = Options()
         options.binary_location ="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Pointing Selenium to Brave's executable
         options.add_argument("--start-maximized")
         options.add_argument("--disable-notifications")
    
         service = Service(ChromeDriverManager().install())
         self.bot = webdriver.Chrome(service=service, options=options)

    def login_fn(self):
        bot=self.bot
        bot.get("https://x.com/i/flow/login")
        time.sleep(5)

        username=bot.find_element(By.NAME,'text')
        username.send_keys(self.user_name)
        next_button=bot.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div')
        next_button.click()
        time.sleep(3)


        password=bot.find_element(By.NAME,'password')
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def autolike(self,hashtag):
        bot=self.bot
        h=hashtag
        bot.get(f'https://x.com/hashtag/{h}')
        time.sleep(3)
        
        wait = WebDriverWait(bot, 10)
        print("waiting for tweets to load")

        try:
            tweets = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//article[@data-testid="tweet"]'))
                                )
            print(f"found all tweets for the hashtag {h}")
        #except Exception as e:
            #print(f"error waiting for tweets:{e}")
            
            for tweet in tweets:
                try:
                
                    like_button = tweet.find_element(By.XPATH,"//div[contains(@aria-label,'Like')]")  
                    aria_label = like_button.get_attribute("aria-label")


                    print(f"Aria label for the like button: {aria_label}")  # Log the aria-label to check its value

                    # Check if the element is inside the viewport
                    if not self.is_element_in_viewport(like_button):
                        print("Like button is not in the viewport, scrolling into view...")
                        bot.execute_script("arguments[0].scrollIntoView(true);", like_button)
                        time.sleep(1)    
                    
                    
                    
                    
                                                                                       
                    
                    if 'Like' in like_button.get_attribute("aria-label"):
                        print(f"Clicking the like button for tweet: {tweet.text[:30]}...") 
                        WebDriverWait(bot, 10).until(EC.element_to_be_clickable(like_button))
                        ActionChains(bot).move_to_element(like_button).click().perform()

                        #like_button.click()  # Click the button to like the tweet
                        print(f"Liked tweet with hashtag {h}")
                    else:
                        print(f"Tweet already liked, skipping: {tweet.text[:30]}...")
                        
                    time.sleep(2)
                except:
                    print(f"error liking tweet with hashtag {h}")
        except Exception as e:
            print(f"error loading tweets for hashtag{h}:{e}")
   
    def close(self):
        self.bot.quit()
            


                                   
        
if __name__ == "__main__":
    twitter_username = "Naxe24"
    twitter_password = "Nanda@x24"
    hashtag = "IshanKishan"  # Hashtag you want to like tweets for

    bot = TwitterBot(twitter_username, twitter_password)
    bot.setup_driver()  # Set up the driver (Brave with ChromeDriver)
    bot.login_fn()  # Log into X
    bot.autolike(hashtag)  # Like tweets with the specified hashtag
    bot.close()
    
        
 #define an object and call the functions   
     



        

        
        

    
