from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['message']
    response = get_bot_response(user_input)
    return jsonify({'response': response})

def get_bot_response(input):
    responses = {
        "hello": "Hi there! How can I assist you with your travel plans today?",
        "where should i go?": "It depends on your interests! Do you prefer beaches, mountains, or cultural experiences?",
        "best time to visit india": "The best time to visit India is generally from October to March, when the weather is pleasant.",
        "popular tourist destinations in india": "Some must-visit places include:\n1. Taj Mahal, Agra\n2. Jaipur\n3. Goa\n4. Kerala\n5. Himachal Pradesh. Would you like recommendations for a specific place?",
        "best time to visit goa": "The ideal time to visit Goa is from November to February. Would you like to know about activities to do there?",
        "what to do in kerala?": "You can enjoy houseboat rides in Alleppey, explore tea plantations in Munnar, or relax on the beaches of Varkala. Interested in any specific activities?",
        "what are some adventure activities in india?": "You can try:\n1. Trekking in Himachal\n2. River rafting in Rishikesh\n3. Scuba diving in Andaman\n4. Paragliding in Uttarakhand. What type of adventure are you looking for?",
        "best cities for food in india": "Cities like Delhi, Mumbai, Kolkata, and Hyderabad are known for their diverse and delicious cuisine. What type of food do you enjoy?",
        "what to pack for a trip to india?": "Packing essentials include comfortable clothes, sunscreen, good walking shoes, and any medications you may need. What season are you planning to visit?",
        "how to get around in india?": "You can travel by trains, buses, auto-rickshaws, and taxis. In major cities, ride-sharing apps are also popular. Do you have a specific city in mind?",
        "is it safe to travel in india?": "Yes, many travelers visit India safely. It's wise to take standard precautions. Are you traveling alone or with a group?",
        "thank you": "You're welcome! If you have more questions, just ask!",
    }

    input = input.lower()
    return responses.get(input, "I'm not sure about that. Can you ask something else?")

if __name__ == '__main__':
    app.run(debug=True)
