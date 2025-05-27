#Jamari Williams
#February 27th,2025
import random
from PIL import Image
import requests
from io import BytesIO

basketballs = [#Molten basketball
               "https://m.media-amazon.com/images/I/91k236NCBBL._AC_SX679_.jpg",
               #Spaldin basketball
               "https://m.media-amazon.com/images/I/91z9BuLRpRL._AC_SX679_.jpg",
               #Franklin basketball
               "https://m.media-amazon.com/images/I/A1IuVyZ1TrS.__AC_SX300_SY300_QL70_FMwebp_.jpg",
               #Wilson basketball
               "https://m.media-amazon.com/images/I/81UNGfmFPHL._AC_SX679_.jpg",
               #Baden basketball
               "https://m.media-amazon.com/images/I/81J1gXLQLKL._AC_SX679_.jpg"]

#baden basketball link on amazon: https://www.amazon.com/Baden-Rival-Game-Basketball-Orange/dp/B09QG6GWB6/ref=sr_1_1_sspa?crid=Q2VF7UL61KXJ&dib=eyJ2IjoiMSJ9.R8w4fdVIsYokxC-Oz3bWwajWrG4Y8Z9JokDGHVfZxqGBINEeMNdIMpJ0y22J8bT__uax7WbVdPjafLjBd4dZIl8RLhI3v-9Xyxj_lEhIn88Pu6Kxkex1HChiw9D1aKMQbUnGKRIpJ_iGI_aXyTtWNEaCDGfZC04TL1XrK7Z74HebUCbgyOy_9BcSC5hgVqYxCgMKrymkb7apA79wvE2-K9Pc15HG897EKJ05k1OkZDZ9Udfz1UcBtiNJfJd5kYlLw7yPmhARfFur1eDHipYPx7Sgz_6kcmdutaaGV2RGkv4.J2g3nSDcCfURVzoYT6ddwxt1iiUJuhUHVL-q83shk7E&dib_tag=se&keywords=baden%2Bbasketball&qid=1740680176&s=sporting-goods&sprefix=baden%2Bbasketball%2Csporting%2C83&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1&psc=1
#Wilson basketball link on amazon: https://www.amazon.com/WILSON-Authentic-Indoor-Outdoor-Basketball/dp/B0D8NQ5122/ref=sr_1_2_sspa?crid=3EBM3YRJJPD5V&dib=eyJ2IjoiMSJ9.bZNWvDzXGJBrgMXXwMFgj1vYPFpLEtrmb3o64nhSJZdmkLsPQ0aDbmlrnK7ZRtTfFhQdwwqx8IGV4Y5qWfd9Ak8pXBZ1ufL0qnHy40YG1ulje49volZc9jxBkuLgGnm6UQMPuNR4tTGSp0cgxNbWrbGs1MOys3Yi70d5GinaM3kbk3cQVghicdA-6ygNiTVSwtdbqoQ7wjojwMqx8dKoCo3yRqiqd3WtD4BmPTn9XlHFVwYVs8MOsyOL--mCM-Zj46LFTOpabqlCeuZLXOZN9kGkdvZgMbwnSRCE3aYOO_w.ISkPusqdt03-se1dAP3kI0SFOnM-ndbeZ1rc_hBLqfg&dib_tag=se&keywords=Wilson%2Bbasketball&qid=1740679680&s=sporting-goods&sprefix=wilson%2Bbasketball%2Csporting%2C89&sr=1-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1&psc=1
#Franklin basketball link on amazon: https://www.amazon.com/Franklin-Sports-5000-Official-Basketball/dp/B07HKX2RR3/ref=sr_1_9?crid=1G1ET7XM4FK3T&dib=eyJ2IjoiMSJ9.NkAB_WWU1CPuY7A7G2yQ7HI-OHDC7gusf8fSXCql_fdfibgYdzvoJo89cdRCtylsjIb9RQyuJ1hKpZcHjbFse6gYQ9F2z3X2DuT8bq0KVUlrS8xiYJ7fP3baMR738-Da1dL1gNEcqPloBU7r5ugHouaOIBInl6PITraWsJ7nn5Gq_PTnH6oDrxVTr4fywbvK9B89IUDYAkibZ_xXFp1eyZqaLUOvAQVgrI12hcD6GRz6262WJ_SSQKb-auRVZsjJ8jPeHKLVDnOcASIntnN4x8NiSIz5SanZBkCjXuX0Jy5nPQC4khueyCRiLY_yL1XVy1lSSPmVmZ0bNhoYABgITJvz9P1NC2Ru71vuxHTSx4c.JsG3mS1G8dIJQTIJxbDgrj4J08Z0Wp2BX_w36zchoUg&dib_tag=se&keywords=Franklin%2Bbasketball&qid=1740679602&s=sporting-goods&sprefix=franklin%2Bbasketball%2Csporting%2C135&sr=1-9&th=1
#Spaldin basketball link on amazon: https://www.amazon.com/Spalding-Precision-TF-1000-Indoor-Basketball/dp/B08QJK6W2W/ref=sr_1_2_sspa?crid=1H7K9MGYK407J&dib=eyJ2IjoiMSJ9.Fnyq1vc6ZPt82pqt-zdOw4OoqBwI5QyZI7w2mQx3gJVEdgOctFTIBqNKl-_S-Y8UxwUDkSKCZO5-b5FF0yIb_JzPpPCyUrP1LcrWNHFEqthubMMFmBJySuQfd-bJihGofJummJjkGTwP8Yo6tO_ZqeJtbc-M9HxcIJ9cdbHQNo8gmRzhzr6GGldSlmb3FBaDtqkvtdG8crWvEypiUxgYXWPf2VdlN-X10JTPVFujMBCRQYoR5D-dU1mOGTdl1P75EY1O9XCFiHuJEkoO53TZJvJYtUe2HrwB-JqBGLrcZBo.AeSkYZbXhRRGsmXLCAgue6mHGGiKOwhDgwbx-rovUjE&dib_tag=se&keywords=spalding%2Bbasketball&qid=1740679485&s=sporting-goods&sprefix=spaldin%2Csporting%2C88&sr=1-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1&psc=1
#Molten basketball link on amazon: https://www.amazon.com/Molten-Leather-Basketball-FIBA-Approved/dp/B085FR47QJ/ref=asc_df_B085FR47QJ?tag=bingshoppinga-20&linkCode=df0&hvadid=80745481717974&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=&hvtargid=pla-4584345025105962&psc=1

#Functions

def open_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()




print("Welcome to basketball recommendations where we help you decide what basketball to play with")

def bball():
    while True:
        rec = input("Ready to hoop?")
        if rec == "yes":
            ball = random.choice(basketballs)
            if ball == "https://m.media-amazon.com/images/I/91k236NCBBL._AC_SX679_.jpg":
                open_image("https://m.media-amazon.com/images/I/91k236NCBBL._AC_SX679_.jpg")
                print("The Molten basketball has been chosen for you")

            if ball == "https://m.media-amazon.com/images/I/91z9BuLRpRL._AC_SX679_.jpg":
                open_image("https://m.media-amazon.com/images/I/91z9BuLRpRL._AC_SX679_.jpg")
                print("The Spaldin basketball has been chosen for you")

            if ball == "https://m.media-amazon.com/images/I/A1IuVyZ1TrS.__AC_SX300_SY300_QL70_FMwebp_.jpg":
                open_image("https://m.media-amazon.com/images/I/A1IuVyZ1TrS.__AC_SX300_SY300_QL70_FMwebp_.jpg")
                print("The Franklin basketball has been chosen for you" )

            if ball == "https://m.media-amazon.com/images/I/81UNGfmFPHL._AC_SX679_.jpg":
                open_image("https://m.media-amazon.com/images/I/81UNGfmFPHL._AC_SX679_.jpg")
                print("The Wilson basketball has been chosen for you")

            if ball ==  "https://m.media-amazon.com/images/I/81J1gXLQLKL._AC_SX679_.jpg":
                open_image( "https://m.media-amazon.com/images/I/81J1gXLQLKL._AC_SX679_.jpg")
                print("The baden ball has been chosen for you")
        if rec == "no":
            print("Enjoy your hoop session")
            break
#Main
bball()
