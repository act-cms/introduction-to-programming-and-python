intro_variable_entry = [
    {
        "question": "Which Python variable assignments will define a float variable?",
        "type": "many_choice",
        "answers": [
            {"answer": "delta_S = 121", "correct": False, "feedback": "Is there a trailing period or decimal places?"},
            {"answer": "R = 8.3145", "correct": True, "feedback": "That is correct."},
            {"answer": "R = 8.206e-2", "correct": True, "feedback": "That is correct."},
            {"answer": "R = '8.206e-2'", "correct": False, "feedback": "Pay close attention to the quotation marks."}
        ]
    }
]

intro_order_of_operations = [
    {
        "question": "What is the value of the variable a that is declared as below? <br><br> a = -1**2",
        "type": "many_choice",
        "answers": [
            {"answer": "+1", "correct": False, "feedback": "Not quite. Which operation, exponentiation or multiplication, takes precedence?"},
            {"answer": "-1", "correct": True, "feedback": "That is correct. Exponentiation takes precendence over multiplication"},
            {"answer": "I have no idea", "correct": False, "feedback": "That is correct."}
        ]
    }
]

intro_int_to_bool_cast = [
    {
        "question": "What is the value of the variable a that is declared as indicated below? <br><br> a = bool(1)",
        "type": "many_choice",
        "answers": [
            {"answer": "1", "correct": False, "feedback": "Not quite. The value of the integer 1 is casted to another variable type."},
            {"answer": "False", "correct": False, "feedback": "Not quite. Refer back to the example above to see the correspondnce between the two boolean values True/False and th integers 1/0."},
            {"answer": "True", "correct": True, "feedback": "That is correct. The boolan value of 1 (or any nonzero integer in Python) is True."},
						{"answer": "bool", "correct": False, "feedback": "Not quite. bool denotes the type of the variable a."}
        ]
    }
]

intro_execution_sequence = [
    {
        "question": "What is the output of the Python code below? <br><br> delta_H = -100.0 <br> delta_S = 0.200 <br> T = 300 <br> delta_G = delta_H - T * delta_S <br> T_eq = -delta_H / delta_S <br> delta_H = -50.0 <br> T_eq    = -delta_H / delta_S <br> print('T_eq    =', T_eq, 'delta_G =', delta_G)",
        "type": "many_choice",
        "answers": [
            {"answer": "T_eq = 500 delta_G = -110", "correct": False, "feedback": "Not quite. At what line were the values of delta_G and T_eq calculted last? What were the values of delta_H, delta_S, and T at that point?"},
            {"answer": "T_eq = 250 delta_G = -110", "correct": False, "feedback": "Not quite. At what line was the value of delta_G calculted last? What were the values of delta_H, delta_S, and T at that point?"},
            {"answer": "T_eq = 500 delta_G = -160", "correct": False, "feedback": "Not quite. At what line was the value of T_eq claculted last? What were the values of delta_H and delta_S at that point?"},
            {"answer": "T_eq = 250 delta_G = -160", "correct": True, "feedback": "That is correct"}
        ]
    }
]

intro_nested_comparison_statements = [
    {
        "question": "What is the output of the Python code below? <br><br> result_1 = ( 1 == ( 4 > 2 ) ) <br> result_2 = ( ( 3 > 2 ) == ( 1 != 2 ) ) <br> print( int(result_1) + int(result_2) )",
        "type": "many_choice",
        "answers": [
            {"answer": "0", "correct": False, "feedback": "Not quite. This would imply that both nested comparisons are False."},
            {"answer": "1", "correct": False, "feedback": "Not quite. This implies that one of the nested comparisons is True while the other is False."},
            {"answer": "2", "correct": True, "feedback": "Correct. Since both nested comparisons are True, the sum is 2."},
            {"answer": "I have no idea", "correct": False, "feedback": "Review the section above to assess your understanding of how nested comparisons are evaluated."}
        ]
    }
]

intro_for_loop = [
    {
        "question": "What mathematical does the code below evaluate? <br><br> i_max = 3 <br> j_max = 5 <br><br> N = 0 <br> for i in range(i_max): <br> &emsp;&emsp; N = N + i <br><br> D = 0 <br> for i in range(j_max): <br> &emsp;&emsp; D = D - i <br><br> R = N / D ",
        "type": "many_choice",
        "answers": [
            {"answer": "$[ \sum_{i=0}^{3} i ] / [ \sum_{i=0}^{5} i ]$", "correct": False, "feedback": "Not quite. Did you check what each for loop 'adds' up?"},
            {"answer": "$ - [ \sum_{i=0}^{5} i ] / [ \sum_{i=0}^{3} i ]$", "correct": False, "feedback": "Not quite. Did you check what the limits are for each for loop?"},
						{"answer": "$ - [ \sum_{i=0}^{3} i ] / [ \sum_{i=0}^{5} i ]$", "correct": True, "feedback": "That is correct."},
            {"answer": "I have no idea", "correct": False, "feedback": "Please go back and re-examine the example of a for loop above."}
        ]
    }
]

intro_numpy_function = [
    {
        "question": "Which statements are correct about the Python math library's comb function (math.comb)",
        "type": "many_choice",
        "answers": [
            {"answer": "Requires two positive integers as input", "correct": True, "feedback": "That is correct"},
            {"answer": "Evaluates the binomial coefficient", "correct": True, "feedback": "That is correct"},
            {"answer": "Requires one positive integer as input", "correct": False, "feedback": "Did you check the documentation using 'help(math.comb)'?"},
            {"answer": "The input must be of type float", "correct": False, "feedback": "Did you check the documentation using 'help(math.comb)'?"}
        ]
    }
]

intro_vectors = [
    {
        "question": "Assuming that v1 and v2 are as defined above, what is the result of the following Python code? <br><br> diff = np.sqrt(v2) - v1 <br> print( diff )",
        "type": "many_choice",
        "answers": [
            {"answer": "[ 0. &ensp;  0. &ensp; 0. ]", "correct": False, "feedback": "Not quite. What is the data type of v1 and v2? The data type of diff will be the same."},
            {"answer": "[ 0 &ensp; 0 &ensp; 0 ]", "correct": True, "feedback": "Element-wise operations return a vector"},
            {"answer": "0", "correct": False, "feedback": "Not quite. Remember element-wise operations return a vector, not a scalar (number)"},
            {"answer": "I have no idea", "correct": False, "feedback": "You should review the description of element-wise operations with arrays given above."}
        ]
    }
]

intro_matrices = [
    {
        "question": "What is the result of the following Python code? <br><br> import numpy as np <br> Nr = 2 <br> Nc = 3 <br> M = np.ones( ( Nr , Nc ) ) <br> B = np.transpose( M ) <br> print( B[ 0 , :] ) ",
        "type": "many_choice",
        "answers": [
            {"answer": "[ 1 &ensp; 1 ]", "correct": False, "feedback": "Not quite. What is the data type of M[0 , 0]?"},
            {"answer": "[ 1. &ensp;  1. ]", "correct": True, "feedback": "Correct. np.tranpose() evalautes the transpose of a matrix so B is a 3x2 matrix, so the 0th row is a vector of length 2"},
            {"answer": "[ 1. &ensp;  1. &ensp;  1. ]", "correct": False, "feedback": "Not quite. What does the function np.transpose() do? Use help() to find out."},
            {"answer": "I have no idea", "correct": False, "feedback": "Please see the documatation of np.transpose() and the description of slices of matrices above."}
        ]
    }
]

intro_quad_integral = [
    {
        "question": "Look at the integrand in the function defined above. Do you notice anything peculiar? Select all that apply.",
        "type": "many_choice",
        "answers": [
            {"answer": " To me, this is just a random function of a single variable x", "correct": False, "feedback": "Not quite. Why do you think we wrote it with the parentheses as indicated?"},
            {"answer": "The integrand is a product of two other functions.", "correct": True, "feedback": "Not bad! But take a closer look at the type of functions inside the parentheses."},
            {"answer": "The function inside each parenthesis is a polynomial.", "correct": True, "feedback": "Not bad! Have we written a general purpose funnction to evaluate the value of a general polynomial?"},
            {"answer": "We already wrote a function to evaluate the value of a polynomial so we can reuse our code!", "correct": True, "feedback": "That is also correct!"}
        ]
    }
]


#QUIZZES = {"num_q": num_q , "many_q": many_q}
