import streamlit as st
import google.generativeai as genai
from reportlab.lib.pagesizes import TABLOID
from reportlab.pdfgen import canvas
from io import BytesIO
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(
    page_title="Destifa - Your Automated Tour Guide",
    page_icon="🌍",
    layout="centered",  # Options: "centered" or "wide"
    initial_sidebar_state="expanded"  # Options: "auto", "expanded", "collapsed"
)
option = st.sidebar.selectbox(
    "Select a section:",
    ["Home", "Tour Info","Chat Bot", "Contact"]
)

if option == "Home":
    st.markdown(
        "<h1 style='font-size: 50px; text-align: center;'>Welcome to Destifa!</h1>",
        unsafe_allow_html=True)
    st.markdown(
        "<h3 style='font-size: 40px; text-align: center;'>Explore your Destination with ease</h3>",
        unsafe_allow_html=True)
    st.markdown(
        "<h2 style='font-size: 50px; text-align: left;'>Developers</h2>",
        unsafe_allow_html=True)
    st.markdown(
        "<h4 style='font-size: 30px; text-align: left;'>1. Parth Khera</h4>",
        unsafe_allow_html=True)
    st.markdown(
        "<h4 style='font-size: 30px; text-align: left;'>2. Mayank Chaudhary</h4>",
        unsafe_allow_html=True)
    st.markdown(
        "<h4 style='font-size: 30px; text-align: left;'>3. Lucky Rawat</h4>",
        unsafe_allow_html=True)
    st.markdown(
        "<h4 style='font-size: 30px; text-align: left;'>4. Pinkesh Kumar</h4>",
        unsafe_allow_html=True)
    st.markdown(
        "<h4 style='font-size: 30px; text-align: left;'>5. Niharika Verma</h4>",
        unsafe_allow_html=True)
elif option == "Tour Info":
    st.title("Tour Information")
    
    # Title for the app
    st.title("Destifa")

    # Sidebar for navigation
    st.sidebar.title("Explore Locations")
    locations = ["Taj Mahal", "Grand Canyon", "Great Wall of China", "Eiffel Tower", "Ram Mandir","Jaipur","Srinagar","Dehradun","Varanasi","Meghalaya","Rameswaram","Vaishno Devi","Shimla","Manali","Delhi"]
    selected_location = st.sidebar.selectbox("Choose a location to explore:", locations)

    # Information about each location
    location_info = {
    
        "Taj Mahal": {
            "description": "A UNESCO World Heritage site in Agra, India, renowned for its stunning white marble architecture and its significance as a symbol of love.",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/da/Taj-Mahal.jpg",
            "best_time_to_visit": "October to March",
            "entry_fee": "₹1100 (approx.) for foreigners, ₹50 for Indian citizens"
        },
    
        "Eiffel Tower": {
            "description": "An iconic symbol of France, located in Paris. Known for its stunning architecture and views of the city.",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3d/Paris_-Tour_Eiffel%28nuit%29.jpg",
            "best_time_to_visit": "April to October",
            "entry_fee": "€25 (approx.)"
        },
        "Ram Mandir": {
            "description": "A major Hindu temple in Ayodhya, India, recently reconstructed and dedicated to Lord Ram, with intricate carvings and significant cultural importance.",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/df/Ayodhya_Ram_Mandir_Inauguration_Day_Picture.jpg",
            "best_time_to_visit": "October to March",
            "entry_fee": "Free"
        },
        "Great Wall of China": {
            "description": "A historic fortification in northern China stretching over 13,000 miles, known for its breathtaking views and remarkable ancient construction.",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/2/23/The_Great_Wall_of_China_at_Jinshanling-edit.jpg",
            "best_time_to_visit": "April to October",
            "entry_fee": "¥40-60 (varies by section)"
        },
        "Grand Canyon": {
            "description": "A massive natural wonder in Arizona, USA, known for its vast size, layered red rock formations, and awe-inspiring views.",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/ae/Grand_Canyon_Horse_Shoe_Bend_MC.jpg",
            "best_time_to_visit": "March to May, September to November",
            "entry_fee": "$35 per vehicle (7-day permit)"
        },
        "Jaipur":{
            "description":"City in India, capital of Rajasthan known for its rich heritage,history,colourful buildingd and also known as pink city.",
            "image_url":"https://upload.wikimedia.org/wikipedia/commons/f/f7/Jaipur_03-2016_02_Amber_Fort.jpg",
            "best_time_to_visit" : "October to March",
            "entry_fee":"FREE"
        },
        "Srinagar":{
            "description":"A city in Kashmir valley of Jammu known for its natural beauty ,houseboat,traditional handicrafts.",
            "image_url":"https://upload.wikimedia.org/wikipedia/commons/a/a8/Houseboats%2C_Dal_Lake%2C_Kashmir.jpg",
            "best_time_to_visit":"March to June",
            "entry_fee":"Depends on the location you are in Kashmir"
        },
        "Dehradun":{
            "description":"A city in the doon valley of uttrakhand,known for its beauty.Also, known as Dev - Bhoomi.",
            "image_url":"https://upload.wikimedia.org/wikipedia/commons/a/ab/Dehradun_district_DSC_7052_%2832696794043%29.jpg",
            "best_time_to_visit" : "August to Febuary",
            "entry_fee":"Free"
        },
        "Varanasi":{
            "description":"Also known as Kashi or Banaras,known for its rich culture ,religious significance and ancient history.",
            "image_url":"https://upload.wikimedia.org/wikipedia/commons/0/04/Ahilya_Ghat_by_the_Ganges%2C_Varanasi.jpg",
            "best_time_to_visit":"October to March",
            "entry_fee":"Free"
        },
        "Meghalaya":{
            "description":"State in northeast India known for its natural beauty,rich biodiversity and dramatic landscape ",
            "image_url":"https://upload.wikimedia.org/wikipedia/commons/e/e8/Meghalaya_Hills.jpg",
            "best_time_to_visit":"June to September",
            "entry_fee":"Free"
        },
        "Rameswaram":{
            "description":"An exquisite temple in the southern India dedicated to lord shiva and a part of twelve jyotirlings.",
            "image_url":"https://upload.wikimedia.org/wikipedia/commons/3/37/Rameshwaram_Ramanadhaswamy_temple.jpg",
            "best_time_to_visit":"October to April ",
            "entry_fee":"Free"
        },
        "Vaishno Devi":{
            "description":"situated in Katra Jammu,dedicated to Mata Vaishno Devi.",
            "image_url":"https://upload.wikimedia.org/wikipedia/commons/b/b0/Snowfall_in_Vaishno_Devi.jpg",
            "best_time_to_visit":"November to  February",
            "entry_fee":"Free"
        },
        "Shimla":{
            "description":"capital of himachal pradesh,known for its natural beauty,colonial architecture,hill station.",
            "image_url":"https://upload.wikimedia.org/wikipedia/commons/d/dd/Shimla_night.jpg",
            "best_time_to_visit":"October to January",
            "entry_fee":"Free"
        },
        "Manali":{
            "description":"popular tourist destination in the Kullu,district of Himachal pradesh,known for its Snow capped mountains,cool weather.",
            "image_url":"https://upload.wikimedia.org/wikipedia/commons/0/03/Manali_City.jpg",
            "best_time_to_visit":"December to February",
            "entry_fee":"Free"
        },
        "Delhi":{
            "description":"capital of India,known for its rich history,Diverse culture,and many attraction(like lotus temple etc..)",
            "image_url":"https://upload.wikimedia.org/wikipedia/commons/6/67/Delhi_red_fort_1.jpg",
            "best_time_to_visit":"October to March",
            "entry_fee":"Free"
        }


    }

    # (Include details for other locations)


# Display location information
    st.header(selected_location)
    info = location_info[selected_location]
    st.write(info["description"])
    st.image(info["image_url"], use_column_width=True)
    st.write(f"Best Time to Visit: {info['best_time_to_visit']}")
    st.write(f"Entry Fee: {info['entry_fee']}")

# User input for travel details
    st.subheader("Plan Your Visit")
    days = st.slider("Select number of days to stay", 1, 30)
    budget = st.number_input("Enter your budget (in local currency)", value=1000)
    st.write(f"You plan to stay for {days} days with a budget of {budget}.")

    if st.button('Generate Travel Guide'):
        genai.configure(api_key="AIzaSyCaXS29dluxHJz382pdLu8maCM9HUMLCe8") 
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }

    # Define the chat session for guide generation
        model = genai.GenerativeModel(
            model_name="gemini-1.5-pro",
            generation_config=generation_config,
            system_instruction='''You are a travel agent...Always give a detailed travel plan and there should be only 22 words in a single
             line, if their are some words left then shift them to next line. Also give a budget summary in last.for international countries convert dollar into indian rupee,also keep the dollar and indian amount''',
        )
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(f"{selected_location}, {budget}, {days} days")
    
        if response and response.text:
            guide_text = response.text.replace("*","").replace("₹","Rs")
            st.write(guide_text)  # Display the guide on the page

        # Generate PDF from guide text
            pdf_buffer = BytesIO()
            pdf = canvas.Canvas(pdf_buffer, pagesize=TABLOID)
            pdf.drawString(20, 1200, f"Travel Guide for {selected_location} from Destifa")
        
            y_position = 1150
            for line in guide_text.splitlines():
                pdf.drawString(25, y_position, line)
                y_position -= 20
                if y_position < 50:  # Start new page if needed
                    pdf.showPage()
                    y_position = 1200
        
            pdf.save()
        
        # Display download button for the PDF

            pdf_buffer.seek(0)
            st.download_button(
                label="Download Travel Guide as PDF",
                data=pdf_buffer,
                file_name=f"{selected_location}_Travel_Guide.pdf",
                mime="application/pdf"
            )
        else:
            st.error("Failed to generate guide. Please try again.")
elif option == "Chat Bot":
    genai.configure(api_key=("AIzaSyCaXS29dluxHJz382pdLu8maCM9HUMLCe8"))
    model = genai.GenerativeModel("gemini-pro")
    chat=model.start_chat(history=[])
    def get_gemini_response(question):
        response = chat.send_message(question,stream=True)
        return response
    #st.set_page_config(page_title="Destifa")
    st.header("Destifa: Chat Bot")

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    input = st.text_input("Input:",key="input")
    submit = st.button("Ask The Question")

    if submit and input:
        response = get_gemini_response(input)
        st.session_state['chat_history'].append(("You",input))
        st.subheader("The Response is")
        for chunk in response:
            st.write(chunk.text)
            st.session_state['chat_history'].append(("Destifa",chunk.text))
    st.subheader("The Chat history is")
    for role,text in st.session_state['chat_history']:
        st.write(f"{role}:{text}")

elif option == "Contact":
    st.markdown(
        "<h2 style='font-size: 40px; text-align: centre;'>Contact</h2>",
        unsafe_allow_html=True)
    #st.markdown(
        #"""<h4 style='font-size: 40px; text-align: left;'>Instagram:</h4>""",
        #unsafe_allow_html=True)
    st.markdown(
        """
    If you have any questions, feel free to reach out at""")
    st.markdown("""
    [kheraparth15@gmail.com](mailto:kheraparth15@gmail.com) or visit our""")
    st.markdown("""
    [instagram](https://www.instagram.com/bug_photografer?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==) and
    """
    )
    st.markdown(
        """Contact Number = 8979800176 for more information.
"""
    )