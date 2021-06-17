import os

import smtplib

import time

import sys



def missiontab():

  t = time.localtime()

  current_time = time.strftime("%H:%M:%S", t)

  print(current_time)

  #if len(sys.argv) != 3:

   # sys.exit('Error')

  TOKEN = os.environ.get('synack_b')

  os.popen("curl -X 'GET' -H $'Host: platform.synack.com' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0' -H 'Accept: application/json' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H 'Referer: https://platform.synack.com/tasks/user/available' -H 'X-CSRF-Token: xxxx' -H 'Authorization: Bearer '"+TOKEN+" -H 'Content-Type: application/json' -H 'Connection: close' -H 'Cookie: visid_incap_1222919=YYaJ/uO3THuM2vfX9hmracmhkF4AAAAAQUIPAAAAAAC7LqBU93apRho44M1pVZhC; visid_incap_1222915=opMu+w7qSymo0oZuIQyMlPKhkF4AAAAAQUIPAAAAAADfT9LTWuP5D9kbfIDduKRU; fs_uid=rs.fullstory.com#QDGY#6340436235403264:4728339087245312#316eef80#/1618072947; visid_incap_2259066=RfZViX9xTJW0gaBYZKvscv2hkF4AAAAAQUIPAAAAAAACWvcWDR4ronRDyptiON15; _ga=GA1.2.646061432.1586742955; _mkto_trk=id:738-OEX-476&token:_mch-synack.com-1586742962786-66456; __q_state_wMSIsrvzp9xgEeyW=eyJ1dWlkIjoiNTNjODE0ZGItMzBjMC00ZTc0LTk1NGYtNjdlMjFlNzMxZWY3IiwiY29va2llRG9tYWluIjoic3luYWNrLmNvbSJ9; intercom-session-chyyq18s=VDNSbnFGd3hXd2FwMmIwSFF5YzRPV1o5b1dFdWFIcytpZ0JKdzNxL2NoNkxnekZ0RENwSGxDUWdXd2VDMUNKRy0tU09ZRnBjVFVQTmlpc0JWQkpHNEFXQT09--c0063cd753366c8b80e08029793873b19d0e00d0; incap_ses_714_1222915=CWc5Ljzo6hzvyWHtaqToCX8CuF4AAAAADZ1mgg/vUSPpk9U0LKLocg==; incap_ses_711_1222919=AUX8Ul3u7VhSLNqm7PvdCa/qt14AAAAAI/BvYx+3zHuJXFw0/vEkWw==; incap_ses_710_2259066=zLGAeLzh4UI62g32gm7aCX4CuF4AAAAAKSZnXs4WQ3wMYi1lq/aHXw==; incap_ses_887_1222915=B/e0BRtz9EQuuxkO90JPDADrt14AAAAAFuRGtadX/5/dBVG5I3a8jA==; incap_ses_886_2259066=uNZ5TdvvwR5GlOCtc7VLDBvrt14AAAAAmJ8EC2bVNlKCBc21809f1A==' -b $'visid_incap_1222919=YYaJ/uO3THuM2vfX9hmracmhkF4AAAAAQUIPAAAAAAC7LqBU93apRho44M1pVZhC; visid_incap_1222915=opMu+w7qSymo0oZuIQyMlPKhkF4AAAAAQUIPAAAAAADfT9LTWuP5D9kbfIDduKRU; fs_uid=rs.fullstory.com#QDGY#6340436235403264:4728339087245312#316eef80#/1618072947; visid_incap_2259066=RfZViX9xTJW0gaBYZKvscv2hkF4AAAAAQUIPAAAAAAACWvcWDR4ronRDyptiON15; _ga=GA1.2.646061432.1586742955; _mkto_trk=id:738-OEX-476&token:_mch-synack.com-1586742962786-66456; __q_state_wMSIsrvzp9xgEeyW=eyJ1dWlkIjoiNTNjODE0ZGItMzBjMC00ZTc0LTk1NGYtNjdlMjFlNzMxZWY3IiwiY29va2llRG9tYWluIjoic3luYWNrLmNvbSJ9; intercom-session-chyyq18s=VDNSbnFGd3hXd2FwMmIwSFF5YzRPV1o5b1dFdWFIcytpZ0JKdzNxL2NoNkxnekZ0RENwSGxDUWdXd2VDMUNKRy0tU09ZRnBjVFVQTmlpc0JWQkpHNEFXQT09--c0063cd753366c8b80e08029793873b19d0e00d0; incap_ses_714_1222915=CWc5Ljzo6hzvyWHtaqToCX8CuF4AAAAADZ1mgg/vUSPpk9U0LKLocg==; incap_ses_711_1222919=AUX8Ul3u7VhSLNqm7PvdCa/qt14AAAAAI/BvYx+3zHuJXFw0/vEkWw==; incap_ses_710_2259066=zLGAeLzh4UI62g32gm7aCX4CuF4AAAAAKSZnXs4WQ3wMYi1lq/aHXw==; incap_ses_887_1222915=B/e0BRtz9EQuuxkO90JPDADrt14AAAAAFuRGtadX/5/dBVG5I3a8jA==; incap_ses_886_2259066=uNZ5TdvvwR5GlOCtc7VLDBvrt14AAAAAmJ8EC2bVNlKCBc21809f1A==' 'https://platform.synack.com/api/tasks/v1/tasks?withHasBeenViewedInfo=true&status=PUBLISHED&page=0&pageSize=20' -o synackoutput.txt --compressed")

  string  =  '{"message":"Forbidden"}\n'

  string1 = '[]\n'

  string2 = ''

  #print string,string;

  string3 = open('synackoutput.txt').read()

  os.popen("rm synackoutput.txt")

  print string3; 

  if string3 == string1: #debug purpouse

     print('equal') 

  else:

     print('notequal')



  if string3 in [string,string1,string2]:

    print('Mission not FOUND')

    status = 1

    if string3 == string1:

       status = 2

      # diffs = mail(status,string)

    else:

       status = 3

       diffs = mail(status,string)

  else:

    status = 0

    print('Mission FOUND')

    print string1;

    diffs = mail(status,string)

  print status; 

  













def mail(status,string):

    if status == 0:

      print "INMAIL"

      os.popen("curl -X POST -H 'Content-type: application/json' --data '{\"text\":\"Mission Avilable!\"}' 'https://hooks.slack.com/services/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'")

    else:

      print "ok"

    if status == 3:

      print "INMAIL"

      os.popen("curl -X POST -H 'Content-type: application/json' --data '{\"text\":\"Mission forbidden. Connection Issue!\"}' 'https://hooks.slack.com/services/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'")

    else:

      print "ok"







def mission_token():

  global mt

  TOKEN = os.environ.get('synack_b')

  os.popen("curl -X 'GET' -H 'Host: platform.synack.com' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H 'Referer: https://platform.synack.com/' -H 'Authorization: Bearer '"+TOKEN+" -H 'Connection: close' -H  'Cookie: visid_incap_1222915=TzHRu9SvTwiEUIcwXGMp7gBjGV8AAAAAQUIPAAAAAAB8YSx5lo26VZSOaHVmdA59; visid_incap_1222919=5YlC9AOLQEO2dqVfQtdWhgBjGV8AAAAAQUIPAAAAAADYnT+YKqmL5aHzUoMYOL4h; fs_uid=rs.fullstory.com#QDGY#6044887422418944:5063476773732352#316eef80#/1627035358; visid_incap_2259066=XP7U+ysKRFmr4XwkFk+rD15jGV8AAAAAQUIPAAAAAABxmzHdewIoeGNuVFmFYssO; _ga=GA1.2.1883377263.1595509574; incap_ses_1211_1222915=bAI5WM8Eogh7FJLEJVbOEIFRK18AAAAAo4xwBIRB+7mLmA+tyt9kpw==; incap_ses_889_1222919=97f5VpWYlXRIEj/X3FxWDIFRK18AAAAA0xlZvqM3lNELnKnLaQikwg==; incap_ses_890_2259066=9ce0UPMlwXjkiJ57W+pZDIBRK18AAAAAMqrO03jkBDOY97vuynxq9A==; _gid=GA1.2.1428005156.1596674450' -b 'visid_incap_1222915=TzHRu9SvTwiEUIcwXGMp7gBjGV8AAAAAQUIPAAAAAAB8YSx5lo26VZSOaHVmdA59; visid_incap_1222919=5YlC9AOLQEO2dqVfQtdWhgBjGV8AAAAAQUIPAAAAAADYnT+YKqmL5aHzUoMYOL4h; fs_uid=rs.fullstory.com#QDGY#6044887422418944:5063476773732352#316eef80#/1627035358; visid_incap_2259066=XP7U+ysKRFmr4XwkFk+rD15jGV8AAAAAQUIPAAAAAABxmzHdewIoeGNuVFmFYssO; _ga=GA1.2.1883377263.1595509574; incap_ses_1211_1222915=bAI5WM8Eogh7FJLEJVbOEIFRK18AAAAAo4xwBIRB+7mLmA+tyt9kpw==; incap_ses_889_1222919=97f5VpWYlXRIEj/X3FxWDIFRK18AAAAA0xlZvqM3lNELnKnLaQikwg==; incap_ses_890_2259066=9ce0UPMlwXjkiJ57W+pZDIBRK18AAAAAMqrO03jkBDOY97vuynxq9A==; _gid=GA1.2.1428005156.1596674450' 'https://platform.synack.com/api/users/notifications_token' --compressed -o mission_token.json")

  mt=os.popen("jq '.token' mission_token.json").read()

  os.popen("rm mission_token.json")







def listing():

  idl = os.popen("jq '.[0].id' listing.json").read()

  action = os.popen("jq '.[0].action' listing.json").read()

  action = action.replace('"', '')

  action = action.replace('\n','')

  #Logic 

  print idl;

  print action;

  tempwa = "onboarded"

  if action == tempwa:

    fl=open("listing.txt", "r")

    statl=0;

    #print id;

    for chl in fl:

      print statl;

      if idl == chl:

        print "No new mission";

      else:

        statl=1;

        os.popen("curl -X POST -H 'Content-type: application/json' --data '{\"text\":\"New Onboarded!!(Notification1) \"}' 'https://hooks.slack.com/services/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'") 

        time.sleep(2)

        os.popen("curl -X POST -H 'Content-type: application/json' --data '{\"text\":\"New Onboarded!!(Notification2) \"}' 'https://hooks.slack.com/services/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'") 

        time.sleep(2)

        os.popen("curl -X POST -H 'Content-type: application/json' --data '{\"text\":\"New Onboarded!!(Notification3) \"}' 'https://hooks.slack.com/services/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'") 

        time.sleep(2)

        os.popen("curl -X POST -H 'Content-type: application/json' --data '{\"text\":\"New Onboarded!!(Notification4) \"}' 'https://hooks.slack.com/services/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'") 

        time.sleep(2)

        os.popen("curl -X POST -H 'Content-type: application/json' --data '{\"text\":\"New Onboarded!(Notification5) \"}' 'https://hooks.slack.com/services/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'") 

    fl.close()

    # File update logic

    if statl==1:

      fl=open("listing.txt", "w")

      fl.write(idl)

      fl.close()

    else:

      print "";

  else:

    print "Not onboarded"



def mission():



  #status=1;

  id = os.popen("jq '.[0].id' notioutput.json").read()



  # mission check logic 

  print id;

  f=open("notilist.txt", "r")

  stat=0;

  #print id;

  for ch in f:

    print stat;

    if id == ch:

      print "No new mission";

    else:

      stat=1;

      os.popen("curl -X POST -H 'Content-type: application/json' --data '{\"text\":\"Mission Avilable!(Notification1) \"}' 'https://hooks.slack.com/services/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'") 

      time.sleep(2)

      os.popen("curl -X POST -H 'Content-type: application/json' --data '{\"text\":\"Mission Avilable!(Notification2) \"}' 'https://hooks.slack.com/services/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'") 

      time.sleep(2)

      os.popen("curl -X POST -H 'Content-type: application/json' --data '{\"text\":\"Mission Avilable!(Notification3) \"}' 'https://hooks.slack.com/services/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'") 

      time.sleep(2)

      os.popen("curl -X POST -H 'Content-type: application/json' --data '{\"text\":\"Mission Avilable!(Notification4) \"}' 'https://hooks.slack.com/services/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'") 

      time.sleep(2)

      os.popen("curl -X POST -H 'Content-type: application/json' --data '{\"text\":\"Mission Avilable!(Notification5) \"}' 'https://hooks.slack.com/services/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'") 

  f.close()

  # File update logic

  if stat==1:

    f=open("notilist.txt", "w")

    f.write(id)

    f.close()

  else:

    print "";



def pro(mt):

  #print mt

  #TOKENIS = os.environ.get('synack_m')

  mt = mt.replace('"', '')

  mt = mt.replace('\n', '')

  #if mt == TOKENIS:

  #  print "Equal MT"

  #else:

  #  print "not equal"

  #print TOKENIS

  #print mt

  result = os.popen("curl -H 'Host: notifications.synack.com' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H 'Referer: https://platform.synack.com/notifications?filter=vulnerability' -H 'Authorization: Bearer '"+mt+" -H 'Origin: https://platform.synack.com' -H 'Connection: close' 'https://notifications.synack.com/api/v2/notifications?filter=campaign&pagination%5Bpage%5D=1&pagination%5Bper_page%5D=1&meta=1' --compressed -o notioutput.json").read()

  

  resultl = os.popen("curl -H 'Host: notifications.synack.com' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H 'Referer: https://platform.synack.com/notifications?filter=vulnerability' -H 'Authorization: Bearer '"+mt+" -H 'Origin: https://platform.synack.com' -H 'Connection: close' 'https://notifications.synack.com/api/v2/notifications?filter=listing&pagination%5Bpage%5D=1&pagination%5Bper_page%5D=1&meta=1' --compressed -o listing.json").read()



  

  notioutput = os.popen("jq '.' notioutput.json").read()

  listioutput = os.popen("jq '.' listing.json").read()

  print notioutput+"\n";

  print listioutput;







  #offerb = os.popen("jq '.results[0].meta.offers_bounties' output.json").read()   

  #minib = os.popen("jq '.results[0].meta.minimum_bounty' output.json").read()

  #bugc = os.popen("jq '.results[0].meta.bug_count' output.json").read()

  #lolw = "lol"

  #test = 

  #print test;

  print len(notioutput);

  if len(notioutput) != 31:

    mission()

  else:

    print "Token Error"

    os.popen("curl -X POST -H 'Content-type: application/json' --data '{\"text\":\"Mission TOKEN ERROR!(Notification) inside Campaign \"}' 'https://hooks.slack.com/services/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'") 



  os.popen("rm notioutput.json")

  #print "END";





  #print test;

  print len(listioutput);

  if len(listioutput) != 31:

    listing()

  else:

    print "Token Error"

    os.popen("curl -X POST -H 'Content-type: application/json' --data '{\"text\":\"Mission TOKEN ERROR!(Notification) inside Listing \"}' 'https://hooks.slack.com/services/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'") 



  os.popen("rm listing.json")

  print "END";



if __name__ == '__main__':

  while True:

    mission_token()

    missiontab()

    pro(mt)

    time.sleep(180)





