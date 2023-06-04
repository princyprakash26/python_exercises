#Scrabble score:

score = {
    'A''E''I''L''N''O''R''S''T''U' : 'one point',
    'D''G' : 'Two points',
    'BCMP' : 'Three points',
    'FHVWY' : 'Four points',
    'K' : 'Five points' ,
    'JX' : 'Eight points' ,
    'QZ' : 'Ten points'
}



program = input('enter the score letter:')

for key ,values in score.items():
    if program.upper() in key:
        print(values)



