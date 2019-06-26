# Install
 The Python used in this project was 3.6.5, you can install the necessary packages by 'pip install -r requirements.txt'.
 
# Optimization Linear Apply in Quantum Computer 

In this project have finally has the purpose to bring a direct conversion of the processes of linear optimization to a quadratic form with application in quantum computers of D-Wave.

In the repository there are three .py files, the file optimize_quantum.py is a class of functions they are:

[1] product_notable\
[2] model_dwave\
[3] result_dwave

The function [1] transforms linear constraints into quadratic functions and sums all constraints, function [2] transforms the final quadratic function into the D-Wave model and finally the function [3] brings the final solution with the lowest energy and the best value that maximizes or minimizes according to the objective function.

The example_article_linkedin.py file runs an example based on the mathematical model below:

![\Large \begin{aligned}
& \text{maximize} & & 7x_1+4x_2+19x_3 \\
& \text{subject to} && x_1+x_3\leq1, \\
& &&   x_2+x_3 \leq1, \\
& &&  x_1,x_2,x_3=0 \enspace or \enspace 1. 
\end{aligned}](https://latex.codecogs.com/gif.latex?%5Cbegin%7Baligned%7D%20%26%20%5Ctext%7Bmaximize%7D%20%26%20%26%207x_1&plus;4x_2&plus;19x_3%20%5C%5C%20%26%20%5Ctext%7Bsubject%20to%7D%20%26%26%20x_1&plus;x_3%5Cleq1%2C%20%5C%5C%20%26%20%26%26%20x_2&plus;x_3%20%5Cleq1%2C%20%5C%5C%20%26%20%26%26%20x_1%2Cx_2%2Cx_3%3D0%20%5Censpace%20or%20%5Censpace%201.%20%5Cend%7Baligned%7D)

Suggestions or constructive criticism send an email to valteresj@gmail.com or rmd2.cin@gmail.com.
