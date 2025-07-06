import random

joke_list = [
    # ----- Hindi Jokes (Written in English Script) -----
    "Teacher: Batao sabse buddhimaan jaanwar kaun hai? Student: Zebra... kyunki wo hamesha line mein chalta hai.",
    "Pappu doctor ke paas gaya, bola: Doctor sahab, mujhe bhoolne ki bimari ho gayi hai. Doctor: Kab se? Pappu: Kab se kya?",
    "Raju: Yaar mujhe neend nahi aati. Amit: Kyun? Raju: Machhar kaat'te hain. Amit: Machhardani kyun nahi lagate? Raju: Machhardani mein kaat'te hain bhai!",
    "Teacher: Tum school der se kyun aaye? Student: Machhli pakad raha tha. Teacher: Aur school mein kya pakadne aaye ho? Student: Number!",
    "Mohan: Shaadi aur jail mein kya farq hai? Sohan: Jail mein khana free milta hai.",
    "Teacher: 'Tera naam kya hai?' English mein bolo. Student: 'What is your name, Tera?'",
    "Baccha ro raha tha. Mummy: Kyun ro raha hai? Baccha: Mobile ka battery khatam ho gaya.",
    "Santa ATM gaya aur likha – Password bhool gaya hoon. ATM bola – 'Mummy se poochh lo.'",
    "Pappu: Tum kaunsi cheez sabse zyada khaa sakte ho? Gappu: Dusre ki plate mein se!",
    "Pyaaz: Main rulata hoon. Lahsun: Main badboo failata hoon. Dhania: Main toh bas sajne aata hoon.",
    "Rahul: Mummy, machhar kyun kaat'te hain? Mummy: Kyunki wo bhi khoon ke rishtedaar hain!",
    "Teacher: Agar prithvi se hawa nikaal di jaaye to kya hoga? Student: WhatsApp band ho jayega!",
    "Pati: Shaadi kyun ki thi tumne? Patni: Taaki pata chal sake dukh kya hota hai!",
    "Teacher: Batao suraj kis disha mein ugta hai? Student: WhatsApp mein dikhta hai sir!",
    "Bablu: Mujhe neend nahi aati. Pintu: Shaadi kar le bhai, neend kya, sapna bhi nahi aayega.",
    "Boss: Late kyun aaye? Employee: Sapna dekh raha tha meeting mein hoon.",
    "Teacher: Tum har baar fail kyun hote ho? Student: Sir, sawaal hi samajh nahi aata.",
    "Baccha: Mummy papa kahan hain? Mummy: Dil mein. Baccha: Matlab main orphan hoon?",
    "Santa: Kal se diet par hoon. Banta: Par haath mein samosa? Santa: Diet par hoon, swarg mein nahi!",
    "Patni: Aapki shirt gandi hai. Pati: Meri life bhi!",
    "Teacher: Batao pakshi kaise ud'te hain? Student: Dar ke maare!",
    "Amit: Bhai shaadi kar le. Sumit: Kyun? Amit: Neend mein bhi 'Yes dear' kehna seekh jaayega.",
    "Doctor: Aapko kya takleef hai? Patient: Takleef yeh hai doctor sahab, takleef hi takleef hai!",
    "Girl: Tum mujhe follow kyun kar rahe ho? Boy: Mujhe guide chahiye life mein.",
    "Pappu: TV mein kuch accha nahi aa raha. Dadu: Toh TV ko khush karo beta.",
    "Chintu: Mummy daant kyun rahi ho? Mummy: Kyunki beta, pyar express karne ke tareeke alag hote hain.",
    "Santa: Mere sapno ki rani kab aayegi? Friend: Bhai swipe left kar, koi toh milegi.",
    "Teacher: Homework kahan hai? Student: Dog kha gaya. Teacher: Purana ho gaya! Student: Dog bhi bored ho gaya tha sir.",
    "Mummy: Beta ro kyun raha hai? Beta: Jarvis ne mere joke pe hasi nahi ki.",
    "Patni: Aap mujhe ignore karte ho. Pati: Kaun ho tum?",
    
    # ----- English Jokes (20) -----
    "Why don’t scientists trust atoms? Because they make up everything!",
    "I told my computer I needed a break, and now it keeps sending me KitKats.",
    "Why was the math book sad? It had too many problems.",
    "I asked the gym trainer if he could teach me to do the splits. He replied, 'How flexible are you?' I said, 'I can’t make it on Tuesdays.'",
    "Parallel lines have so much in common… it’s a shame they’ll never meet.",
    "Why don’t programmers like nature? It has too many bugs.",
    "Why did the computer go to therapy? It had too many bytes of sadness.",
    "Why did the scarecrow win an award? He was outstanding in his field!",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "I told my friend 10 jokes to make him laugh. Sadly, no pun in ten did.",
    "Why did the developer go broke? Because he used up all his cache.",
    "I asked my dog what’s two minus two. He said nothing.",
    "My internet is so slow, it’s just faster to run to the library.",
    "I would tell you a UDP joke... but you might not get it.",
    "Why was the JavaScript developer sad? Because he didn’t 'null' his feelings.",
    "Why do Java developers wear glasses? Because they don't C#.",
    "I accidentally swallowed some food coloring. The doctor says I’m okay but I feel like I’ve dyed a little inside.",
    "How does a penguin build its house? Igloos it together.",
    "Why can’t your nose be 12 inches long? Because then it would be a foot!",
    "I ate a clock yesterday. It was very time-consuming."
]

#Function to tell a random joke from the joke_list
def tell_joke():
    return random.choice(joke_list)