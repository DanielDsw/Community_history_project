# does the unpackaging
import streamlit as st

# image compiling
from PIL import Image

# imports functions
from func import*

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Home","Early Life","Marriage","Children","Immigration","Bibliography"])

# 1 Home

with tab1:
  st.caption("Community History Project / Home")
  
  h("Introduction", "David Zhang, my granpa, was born in southern China. The reason I chose him as my subject is that I didn't know much about his past, and wanted to know more.")
  
  image1 = Image.open("beach.jpg")
  st.image(image1,"(1) A photo near the beach. On the right is my subject, and on the right is me!")

  sh("About","I've always looked up to my granpa; he's brave, talented, and wise. Though, he rarely speaks of his past. So, I conducted an oral interview to learn more about how he came to be. Using the info from the interview and various other sources, I created this website to present the history of David Zhang!")
  
  st.write("But before that, here are some things that I knew before I started this project, so that we can see how his hobbies connect with his past!")

  col1, col2, col3 = st.columns(3)
  with col1:
    st.subheader("Hobbies")
    st.write("Gardening")
    st.write("Fishing")
    st.write("Excercising")
    st.write("Taking walks")
  with col2:
    st.subheader("Belongings")
    st.write("Glasses")
    st.write("An old family photo")
    st.write("An old watch")
  with col3:
    st.subheader("Other")
    st.write("Lived in a small villa in southern China")
    st.write("Had a fishing boat in the village")
    st.write("Enjoys watching war movies")
    
  st.divider()
  
# 2 Early Life

with tab2:
  st.caption("Community History Project / Early_Life")
  h("Background info","In the southern region of China (Cantonese region), aside from the urban areas, plantations and farmlands take up a lot of the land. And, my subject happened to have grown up near one of these. In fact, his family owned one.")
  
  image2 = Image.open("plantation.jpg")
  st.image(image2,"(2) This is an image of a plantation that's similar to the one he described.")

  sh("Early Life","David was born in a small village, his family owned several small houses. He has 7 siblings, although, most of them weren't in the house much.")
  st.write("As the second oldest in the house, David had to set an example for his younger siblings; he had to do most of the chores. And because of this, he had to learn various skills like fishing, farming, and swimming. There was also a mall that he would occasionally talk about. He would explain how he would always go there to get snacks and hang out with his close cousins. But since the villa was on a mountain, he had long commutes.")

  image3 = Image.open("topo.jpg")
  st.image(image3,"(3) Above is a map of the topography in the lower region of China. The scale represents the altitude, the height of land above surface level.")

  sh("Location","Judging from his description of the mountains, the village is likely located on the left side of this map.")
  
  st.divider()
  
# 3 Marriage
  
with tab3:
  st.caption("Community History Project / Marriage")
  h("Marriage","In April 17, 1973, David Zhang decided it was time to truly start his life. He was the first of his brothers to marry and have kids.")
  
  image4 = Image.open("pumpkin.jpg")
  st.image(image4,"(4) On the far left, is me, and the person sitting in front of me is my subject's wife. This photograph was taken on their 45th anniversary.")

  st.subheader("Immigration")
  st.write("It was during this time when he started considering moving to America for a better life for his children. He thought that if they moved to America, his children would be able to find better jobs and get a better education.")
  
  st.divider()
  
# 4 Children

with tab4:
  st.caption("Community History Project / Children")
  h("Children","My subject had two daughters, Ema (my aunt), and Zinmei (my mother).")

  image5 = Image.open("d.jpg")
  st.image(image5,"(5) On the far left, is my aunt. The one standing in the back with the orange shirt is my mother.")

  sh("Birth","Ema was born first, then my mother was born in August 27, 1983 (Both born in China). My mother was born in Zhongshan.")
  sh("School","Both my aunt and my mother went to a public school. They both attended 'Lower East Side Prep School'. After they both graduated, they attended college, but never graduated. Ema went to 'CUNY Manhattan' and my mom went to 'New York City College of Technology.'")

  image6 = Image.open("lesp.jpg")
  st.image(image6,"(6) This image shows the high school that my subject's daughters attended.")

  image7 = Image.open("CUNYM.jpg")
  st.image(image7,"(7) This image shows the college that my aunt attended.")

  image8 = Image.open("NYC_Tech.jpeg")
  st.image(image8,"(8) This image shows the college that my mother attended.")
  
  st.divider()
  
# 5 Immigration

with tab5:
  st.caption("Community History Project / Immigration")
  h("A new life","Shortly after David's daughters graduated from middle school, they decided to start a new life in America. And so, they moved to a house near Sunset Park.")

  image9 = Image.open("brooklyn.jpg")
  st.image(image9,"(9) The map above shows the neighbourhoods of brooklyn. On the left, above Bay Ridge, is Sunset Park, where they first moved from China. Towards the center is Kensington, where they moved after that.")

  st.subheader("Challenges")
  st.write("One major issue that they faced was the language barrier. None of them knew how to speak or understand English. This was an exceptionally big problem for the daughters since they couldn't really communicate with teachers, the locals, nor other students.")
  st.write("Another issue was initially looking for a job. Since David couldn't do a job that involved speaking English, he decided that he could become a truck driver. He had to first, obtain a driver's liscense, then look for the job. The problem was that they barely able to sustain a stable income. This lasted for several months.")

  st.subheader("Moving (again)")
  st.write("A few years after I was born, they moved yet again to the Kensington neighbourhood. David retired in 2020.")
  
  st.divider()
  
# 6 Bibliography

with tab6:
  st.caption("Community History Project / Bibliography")
  h("Sources","(1) A photo near the beach. On the right is my subject, and on the right is me!")
  
  st.write("(2) https://www.bloomberg.com/news/features/2017-02-21/australian-sandalwood-plantation-is-about-to-make-its-owners-a-lot-of-money This is where I got the image of the plantation from (There aren't any photos of the actual one).")

  st.write("(3) https://www.researchgate.net/figure/Topographical-map-m-of-southern-China-The-red-text-in-the-figure-is-the-names-of_fig1_347426695 This is where I got the map of the topography in the lower region of China.")

  st.write("(4) A photo taken on a farm, during pumkin season.")

  st.write("(5) A photo taken in our current backyard.")

  st.write("(6) https://nycmentors.org/schools/lower-east-side-preparatory-high-school This image shows the middle/high school that my subject's daughters attended.")

  st.write("(7) https://www.unigo.com/colleges/cuny-borough-of-manhattan-community-college This image shows the college that my aunt attended")

  st.write("(8) https://structurae.net/fr/ouvrages/new-york-city-college-of-technology This image shows the college that my mother attended")

  st.write("(9) https://www.map-illustrators.com/products/brooklyn-neighborhoods-map This image shows the neighbourhoods of brooklyn")

  st.write("Oral history conducted on 9/17/23. Subject: David Zhang, Interviewer: Daniel Dasilva Weng")
  
  st.divider()
  