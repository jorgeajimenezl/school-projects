import math, os, glob
import subprocess
from fractions import Fraction

def get_fraction_str(x: Fraction):
    if x.numerator == 0:
        return "0"
    if x.denominator == 1:
        return str(x.numerator)
    return r"\frac{%d}{%d}" % (x.numerator, x.denominator)

def get_latex_mat(m):
    r = "\\begin{bmatrix}\n"

    for i in range(len(m)):
        r += " & ".join(map(get_fraction_str, m[i]))

        if i != len(m) - 1:
            r += r" \\" + '\n'
        else:
            r += '\n'

    r += "\\end{bmatrix}\n"

    return r

def lineal_transition(a, b, i, j, cf1):
    r = "\\begin{equation*}\n"
    r += get_latex_mat(a)
    r += "\\underrightarrow{\\ \\ \\ f_%d = %s \cdot f_%d - f_%d \\ \\ \\ }" % (j, get_fraction_str(cf1), i, j) + '\n'
    r += get_latex_mat(b)
    r += "\\end{equation*}\n"

    return r

st = [
    [1, 2, 3, 1, 4],
    [2, 5, 7, 5, 9],
    [3, 7, 11, 8, 14],
    [1, 5, 8, 18, 9]
]
st = list(map(lambda x: list(map(Fraction, x)), st)) # Convert to fraction

n = len(st)
latex = ''

for i in range(n - 1):
    for j in range(i + 1, n):        
        cp = st[:] # get copy
        if st[i][i] == 0 or st[j][i] == 0:
            continue
        fact = st[j][i] / st[i][i]        
        for k in range(i, len(st[i])):           
            st[j][k] = fact * st[i][k] - st[j][k]

        latex += lineal_transition(cp, st, i, j, fact)

with open("./algebra/template.tex", 'r') as file:
    template = file.read()

with open("steps.tex", 'w') as file:
    file.write(template % latex)

r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "steps.tex"], 
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if r.returncode != 0:
    print("Error building pdf document. See build.log for more information.")
    with open("build.log", 'w') as file:
        file.write(r.stderr)
        exit(1)

trash_extension_files = ["*.log", "*.aux", "*.dvi", "*.fls", "*.fdb_latexmk", "*.xdv"]
for extension in trash_extension_files:
    for x in glob.glob(extension):
        os.unlink(x)    

print("Successful pdf build")