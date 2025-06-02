# simplex-method

The program implements simplex method for linear programming problem.Method works with any forms of equalities or inequalities transforming problem in canonical form.Simplex method works only with canonical form of linear programming problem.  

Some more information about algorithm:
A system of linear inequalities defines a polytope as a feasible region. The simplex algorithm begins at a starting vertex and moves along the edges of the polytope until it reaches the vertex of the optimal solution.
![image](https://github.com/user-attachments/assets/6235584b-3d77-4cc2-8d43-394902e8cfe9)

\documentclass{article}
\usepackage{listings}
\usepackage{xcolor}

\definecolor{codegray}{gray}{0.9}

\lstset{
    backgroundcolor=\color{codegray},
    basicstyle=\ttfamily\small,
    keywordstyle=\color{blue}\bfseries,
    commentstyle=\color{green!50!black},
    stringstyle=\color{orange},
    showstringspaces=false,
    breaklines=true
}

\begin{document}

\section*{Пример кода на Python}

\begin{lstlisting}[language=Python, caption=Пример функции вычисления факториала]
def factorial(n):
    """Рекурсивная функция для вычисления факториала числа n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
\end{lstlisting}

\end{document}
