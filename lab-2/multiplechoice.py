import random
import time
import hashlib
import itertools
from IPython.display import Image, display, clear_output
from ipywidgets import widgets
from IPython.display import HTML
from ipywidgets import TwoByTwoLayout

#solution = hashlib.md5('soln_str'.encode()).hexdigest()

def si330_labs_mcq(prob_no):    
    num_questions = 3
    choices = 'ABCD'
    solution_hash = 'eccb0954fca9f2005aea084605df5ee9'
    question_text = [
        widgets.HTML(value="""All of the following code snippets will yield a list with the same numbers except for one implementation.
                              Can you identify which one? (assume numpy has been imported)"""), 
        widgets.HTML(value="""Given <pre>
                       arr = np.array([3, 3, 3, 3, 5, 5, 5])
                       mask = np.array([True, True, True, True, True, True, False])
                       
                       intermediate = arr[mask]
                       final_result = intermediate[intermediate > 4]</pre>,
                     what is final_result?"""),
        widgets.HTML(value="""Consider the following dataframe:<pre>
                df = pd.DataFrame([{'fish': 'black bass', 'price': 300}, 
                                   {'fish': 'horse mackerel', 'price': 150}], index = ['river', 'sea'])
        </pre> Which option would NOT correctly compute the total price of both fish?"""),
    ]
    options_text = [
        ### QUESTION 1 #####################
        [widgets.HTML(value="""
        <mark><b>A.</b></mark>
        <pre>
            arr = np.array([[1,2,3],[4,5,6]])
            list(np.arange(10, 20, arr.ndim))
            
        
        </pre>"""), 
        widgets.HTML(value="""
        <mark><b>B.</b></mark>
        <pre>
            arr = np.array([[1,2,3],[4,5,6]])
            list(range(10, 20, arr.shape[0]))
            
        </pre>"""), 
        widgets.HTML(value="""
        <mark><b>C.</b></mark>
        <pre>
            arr = np.array([[1,2,3],[4,5,6]])
            list(np.arange(10, 20, arr.shape[1]))
        
        </pre>"""), 
        widgets.HTML(value="""
        <mark><b>D.</b></mark>
        <pre>
            arr = np.array([[1,2,3],[4,5,6]])
            list(np.linspace(10, 18, 5))
        
        </pre>""")], 
        
        ### QUESTION 2 #######################
        [widgets.HTML(value="""
        <mark><b>A.</b></mark>
        <pre>
            [5, 5] 
        
        </pre>"""), 
        widgets.HTML(value="""
        <mark><b>B.</b></mark>
        <pre>
            [0, 0, 0, 0, 5, 5, 0]
        
        </pre>"""), 
        widgets.HTML(value="""
        <mark><b>C.</b></mark>
        <pre>
            [3, 3, 3, 3, 5, 5]
        
        </pre>"""), 
        widgets.HTML(value="""
        <mark><b>D.</b></mark>
        <pre>
            [0, 0, 0, 0, 5, 5]
        
        </pre>""")],
        
        ### QUESTION 3 #######################
        [widgets.HTML(value="""
        <mark><b>A.</b></mark>
        <pre>
            df.loc['river', 'price'] + df.loc['sea', 'price']
        
        </pre>"""), 
        widgets.HTML(value="""
        <mark><b>B.</b></mark>
        <pre>
            sum(df['price'])
        
        </pre>"""), 
        widgets.HTML(value="""
        <mark><b>C.</b></mark>
        <pre>
            df.iloc[1]['price'] + df.iloc[0]['price']
        
        </pre>"""), 
        widgets.HTML(value="""
        <mark><b>D.</b></mark>
        <pre>
            df.iloc['river']['price'] + df.iloc['sea']['price']
        
        </pre>""")]
    ]
                    
    correct = random.choice(choices)

    possible_hash = {hashlib.md5(''.join([i for i in x]).encode()).hexdigest(): ''.join([i for i in x]) 
                     for x in itertools.product(choices, repeat=num_questions)}
    correct = possible_hash[solution_hash][prob_no]
    answered = False

    
    display(question_text[prob_no])
    display(TwoByTwoLayout(top_left=options_text[prob_no][0], top_right=options_text[prob_no][1], 
                   bottom_left=options_text[prob_no][2], bottom_right=options_text[prob_no][3]))
    time.sleep(1)

    buttons = [widgets.Button(description = choice) for choice in choices]

    container = widgets.HBox(children=buttons)
    display(container)

    status = widgets.HTML(value="")
    display(status)
    
    def on_button_clicked(b):
        nonlocal answered
        if not answered:
            choice = b.description
            b.color = 'white'
            b.button_style = 'success' if choice == correct else 'danger'
            if choice == correct: 
                status.value = "Correct!"
            else:
                status.value = "Incorrect. Please try again."
            answered = True
#                 container.close()
#                 clear_output()
#                 si330_labs_mc(prob_no)
    
    for button in buttons:
        button.on_click(on_button_clicked)