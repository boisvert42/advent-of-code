#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 21:55:27 2021

@author: aboisvert
"""

#%%
'''
The navigation subsystem syntax is made of several lines containing chunks. There are one or more chunks on each line, and chunks contain zero or more other chunks. Adjacent chunks are not separated by any delimiter; if one chunk stops, the next chunk (if any) can immediately start. Every chunk must open and close with one of four legal pairs of matching characters:

If a chunk opens with (, it must close with ).
If a chunk opens with [, it must close with ].
If a chunk opens with {, it must close with }.
If a chunk opens with <, it must close with >.
So, () is a legal chunk that contains no other chunks, as is []. More complex but valid chunks include ([]), {()()()}, <([{}])>, [<>({}){}[([])<>]], and even (((((((((()))))))))).

Some lines are incomplete, but others are corrupted. Find and discard the corrupted lines first.

A corrupted line is one where a chunk closes with the wrong character - that is, where the characters it opens and closes with do not form one of the four legal pairs listed above.
'''

_input = """
{[[((<<[[<[<{(()[])([]{})}({[]<>}{<>()})><{<()[]>>{({}())({}{})}>]>{<{<(<><>)<<>()>><{(){}}<{}>>}(<{{}()}><
[{{([{[({((<[{<><>}]><<({}())((){})>{[[]]{{}<>}}>){{({{}<>}<{}[]>){{[]()}(<>)}}<[[<><>](<>[])]{{
[([{<[(<[(((<<{}<>><()<>>>[([]())[{}<>]])[<<<>>[[]<>]>{[<>()]}])[({<{}[]><[]<>>}<(<>[])<()()>>)
{<({{<<[<{{((<<>{}><{}()>)<<()()>>)}}<<({(()[])[()<>]}([[]<>]))[[<(){}>[[]{}]]<<<>[]>>]>[<[({}
{[[[([[<(<<(([[]()]<()[]>)[<[][]>{<>}])<({<><>}<{}{}>)[<<>{}>{[][]}]>><({[<><>][<>()]}[((){}]<[][]>]){([<
[{<[([{{<[<{<{[]()}(()[])>[[[]<>]<[]{}>]}{[{(){}}](<<>[]>{(){}})}>]>}([{[[{([]())<(){}>}<[<>[]
{(((<{[<{[{<{{[]{}}}{(<>[])<<><>>}>}{({(()())({}[])}([[]{}][[][]]))<<<(){}>[<>{}]><[<>{}]<()[]>
<(((<<({[<([{([][])<[][]>}[{(){}}{<><>}]]<<{()()}<<><>>>>)><[[({{}()}(()[]))[([]())<<>()>]]]{{{({}())[{}<
[(({[[[[<(([{<()()>[<>[]]}({()<>}<<>{}>)]){{[<[]()>[[]<>]][(<>[])<{}<>>)}})>]]]]})[({<[{({[[<{<>}(()
[{<(<<{<<[{<<<<>[]>([][])>>([{[]{}}(()[])]([{}<>](()[])))}]><[({<[{}()]{()[]})(<{}()>{[]{}})}{{[{}()][{}[]]}}
[<([[<(<{[(([{{}[]}<()[]>][<(){}>{{}[]}])[(<{}{}><<>[]>)<([]()>>])][{{{({}[])([][])}<[<>()]{[]<>}>}{<(()<>)[{
{({([{<<[[{<[(<><>)<[]{}>]<<()<>>>>[[({}<>)[{}()]]{[{}<>][[][]]}])[({{()[]}<[][]>}{<<><>><{}[]>})
({<<{[[{([[[<{<>()}[()[]]>{({}())<[]{}>}]<(((){})({}{})){{[]()}({}{})}>]((<({}[])(()())><([]{})(<>(
{{{(({{{<{<{(<<>[]>[<>()])}[[<{}()>]}>([[<<>()><{}[]>]]{{{<>[]}<[]<>>}{(<>[])[<><>]}})}>}{{(<[{<
(<{[{<({[[{[(<<>[]>{(){})){[<><>]}][{{{}{}}(<>[])}{[[]<>][<>()]}]}]{[{{(<>[])<<>()>}}[{([]<>){{}[]}}(<<>
{<([<<{((([([<{}<>>[[]()]]{(()[])(()<>)})<[[()<>][{}{}]]>]({{[[]()](<>{})}{(()[])}}<{<[]{}>{()<>}}[([]()){{}
(({<<[[({[[<((()()))>({<[]()>{[]())}{[<>()]{(){}}})]<<{[[]<>]<()[]>}({{}[]}[[]{}])>({{{}<>}[<
[{[(<<<{({<[<{<>()}>[[(){}]{[]()}]][(<<>[]>{<><>})(([]())[[]{}])]>[({{<>{}}}<<(){}>[<>[]}>)({{{
[{((<<{<[[{{[([]{})[[]()]]<([][]){()}>}{<{<>{}}<()[]>><<<><>>[[][]]>}}[([[<>][<>[]]))(<({}
((([[[<[({{[{{[]()}}]<<<<>[])[{}()]>>}<[[{{}()}{[]()}]<{<>[]}{()<>}>][[[<>{}][{}[]]]]>}{([(<(){}>([]<>)
(<{[[({[<((<(<<>[]>[()[]]){<<>[]><{}{}>}>))>]}([[[[[<(()<>)>(((){}){<>()})]<<<[]()>{[]<>}>[[[]
<[<[([{<{({<[({}<>)<{}<>>]{<<>>}><[<<>[]>{{}<>}]{<(){}><{}{}>}>}){[([<()<>>](<[]<>>))<{({}{})<<>()>}]](
[[(([<{{({<{{{<><>}(()())}(<{}<>>)}{<{[]()}{()()}>[[()()][{}()]]}>})(<{<[<{}()>([]<>)]{([]<>)}>}>{[<({()[]}<
(<(({(<[[(((<<<>{}>(<>[])>((()<>)<{}[]>))){[(<<>[]>{[][]})]{[{(){}}[[][]]]{<[][]>}}})]([{((
[<{{[<(([<[<([<>()]{<>})([{}{}][{}[]>)>(<[{}[]]{[][]}>[{(){}}({}{})])]>([{[[{}[]]][<<>{}>[()<>]]}{[<{}
({[[{{({[[<<({{}}{[]()})<<<><>>[(){}]>>[<<{}{}>{<>[]}>]>]<[[{[[]]{<>{}}}]{{<<>[]><[]()>}{[{}<>]<()<>>}
(<<((<[([({[[{{}()}<()<>>]({{}<>>([]()))]<{(()())((){})}{[[]<>]{{}{}}}>}<[[[<>]<<><>>]<[(){}][<>()]>]
<(({((<(({[{{{{}()}(<>[])}}]{<<[[]{}]([]{})><(()[])[(){}]>>[{(<>()){[]{}}}<<[]<>>[()()]>]}}({[[<
<{<[[{<{[<{<((<>[])[<>{}])><({{}{}}[()<>])>}([{({}{}){{}[]}}{{<>()}[<>()]}])>{{[[({}[])<{}[]>]
[[<{(((<[<{<[<[][]><[][]>][([][])]>}({<[{}()]<[]<>>>})>]([<[[([]<>)]<{()<>>>]<{(()())}>>]<[
<[({([([([<{<<[][]>{{}<>}><<()><<>()>>}{{([]<>){[]{}}}}>[[[[[]][<>[]]]]]]{[{<(()<>)<{}()>>}
[<[{{({[<<[<(([][]){[]{}})((<>())<()[]>)>({[{}<>](<><>)}<<<><>>[{}()]>)][{<{<>{}}[{}()]>[[{}[]>[(){}]]}(((
{<{({<[<[({{<{<><>}{{}{}}>[{<><>}<<>{}>]}{{[()<>](<>{})}{<[][]><<>{}>}}})<({(([]()))<<[]{}>{{
([({<[<{<(<[(<{}{}>{{}<>})[({}[])(<>{})]]([[[][]][{}]])><(([(){}](<>{}))){(<[]<>>[<>{}])}>)][({{((()[])((
(<{[(<<({{{{[<<><>>{<>[]}]}{{<[][]>[{}<>]}<[{}<>]({}())>}}[{({()()}({}()))[[<>[]][<>[]]]}{<<[]()><<>
(({((<(<{{[{(([]<>)[{}()])((()[]))}[<([]<>){()<>}>]])[<{({{}[]}({}<>))<[<>()](<>())>}>{<{[{}[]](<>[])}[{[][]
<[<[<<<<([{{{(()())<[]()>}{[[]<>][<><>]}}(<{()[]}<{}()>><([]{})[{}{}]>)}[[<{[]{}}([]<>)>][[[<><>]<<>{}>]({{}
<<{((({<[[<[<{<><>}<{}{}>>]>]]{{(<([<>()]{{}})><{{[]{}}{()[]}}[<[]()>[[]]]>)<{{(()[])([]())}[[()[]][
[{<<<{{{(<<(({<>[]}[{}()])<[[]{}]>)[[[{}[]]{{}()}][([][]){{}[]}]]>>)}}}>>><(((({{<[{([[]<>]{[][]})[<()()>[{}{
((<[([<[([{{[[{}{}][(){}]](([][])(<><>)>}{<(<>{})(<>{})>}}[(<[()<>]><[{}()](<>())>)<{[[]<>]<(){}
({{[<<([[<([[<<><>>[[]]]{(<>{}){()<>}}]([{(){}}[(){}]]([[]<>]<{}<>>)))[{([{}[]][{}[]])[(()<>)(<>)]}[
({[[{<[<[[[<[(<>[])<()>][([]())]><[([]<>)<<>{}>]>]{{({()<>}{(){}})[{<><>}(()[])]}}]({[<{{}()}<()()>>[
{[<((([[{({[([[][]][[]<>])([[]<>][<>()])]{[[()[]](<><>)]}}{{(<[]()><{}{}>)[<()[]><[][]>)}<{{<><>}{<>[]}
(([{([[{[([[((<><>)<<>()>)<[[]]>]<([()]<<>{}>)[({}())<<>>]>]((<<<>()>{()()]>{{{}}})[{<<>()>({}())}
[<<[[<<<(<([[{()[]>[[]()]]([(){}](<><>))]{<{[]{}}((){})>{{[]}[{}]}})>{(<(([][]))({()()})>(<([]<>)({}<>)>)
<(<(<({({(<<([[]<>]{{}<>})({[][]}[()()])>>{[<<(){}>[{}<>]>{({}{})(<>())}]{<<<>[]><<>()>><{<><>}{()<>}>}})<
<{<<{[<[([<<[[{}](<>{})]{<(){}>{()()}}><{([]<>)}]>]<{{<{(){}}<<>{}>>}}{{<[[][]][<>{}]><(())({}{})>}[{[
({(<<<<([<{{{([]{}){(){}}}[[(){}]])[<{<>()}[{}<>]>{<[]>}]}>{[{[[{}{}][{}[]]](<{}[]><()()>)}
(([{<<[{{<[({<[]>[<>[])}({{}()}{()()}))](<((<><>)[{}[]])<<[]<>>((){})>>({<{}()>}))>{[<([{}<>]<[]<>>)[((){
{{[[<{[[<<{(<<<>()>{{}]>(<{}[]>([][])))<{[{}{}]{(){}}}([[]{}])>}[{<({}[]){()()}>}[[<()[]>{()<>}]
{([<<<<[(((<(<{}()>)((()[]){[][]})>{({[]}(()()))[{[][]}[{}{}]]})(<{[()()]([][])}><{(()[])<()<>>}<{(
((([<<[{{(<(<{[]}<()<>>>(([]())({}())))>)}<[({<{<>()}(<>{})>])]>}]{[[{<{[[<>[]]<<>{}>]{[{}()][{
(({{[({<<({{[{<><>}(())][[()]<{}{}>]}{{[()[]]{{}{}}}[<[][]>{()()}]}}{{(<[]()><[][]>)([[][]]({}<>
([{{([((([({{<[][]>[{}()]}{([]<>)<[]()>}}<{[()()]{<>()}}>)<<([<><>](()()))[(()())<(){}>]>>]){[
[((({([(<{[({{<>()}{[]}}{([]<>](<>[])}){[(()[])[[]]][([][])[<>]]}]{<<{[]()}(<>{})><{{}[]}[<>(
<{{(<<{<((([[{<><>>]<[{}<>]((){})>]{[[()<>]{{}()}]<{[]}<<>()>>})<<[[[][]]{[][]}]{{{}[]}<()
<({(<({({[(<[[<>{}]<<>[]>]>(<[[]()][()()]>{<(){}>[[][]]>)){<{{{}}}<({})<{}()>>>{{{()<>}<[]<>>}(<()
({<<([<<<[{<([[][]]{[]<>})<<<>{}>((){})>>}{{<(<>[])[<>()]><([][])(()())>}[[{[]<>}{()()}]{({}{}){{}{}}}]}]{{(
{{{<{[({[[<[([()[]])<<{}[]>{()[]}>]>]((<({<>()}<[]<>>)[{<>[]}]>[{[()<>]<<>>}<{()()}{{}[]}>
({<[[<<([<{{[<[][]>{{}{}}]{[[]()][[]()]}}<{{{}{}}<{}[]}}[{()<>}(()[])]>}[([(<>())]){(<[]()><<>()>)}]
{<{((<<{<({<<{{}<>}{<>[]}>[{[]<>}{()}]>([(<>[]){{}{}}][[<>{}](<><>)])}[(<[[][]]({}[])><<<>{}]>){<[{}[]]<
(([<[<{<({<[{[()()]<{}<>>}{<<><>>{()<>}}]{{(()[])[[]<>]}<({}{})<{}[]>>}>({({<><>}[{}<>])(<()<>>)}[(<{}(
[{<<<<[[{{<{([[]()]<[]<>>)}>{<({()()}<{}[]>)>[{{[][]}[{}<>]}({<><>}(<>()))]}}{[[{<<>{}>><([]())(()
{([(<{{[{{[((<[]()>[{}<>])(<{}<>>[(){}>))]([<<[]<>>[<>[]]>{{[][]}{{}{}}}]{<({}{}){<>[]}>([<>
[<{[{(((({<[{{{}{}}[[]<>]}[{[]<>}<(){}>]]<{({}())[()<>]}<<[]()>([][])>>>([<<()[]><()<>>>]<([()<>][<>[]
{<{[{<<{<<{(((<><>)[[]()]){({})<[]()>})[[<<>{}>(<>())]<(()<>){[]()}>]}{{<({}[]){(){}}>{[()<>]({}{})}}}>>[[
(({<<{{<[<<<<[[]<>]<[]{}>>[((){})({}[])]>[<(<>())([]{})><[{}<>][[]{}]>]>((([<>[]]<<>[]>)([<><>][[][]]}))>][(<
[[{<{{{(([{({([]<>)[<>[]]}{[[]<>][()<>]}){{<<>()>([]{})}[{<>()}(<><>)]}>(([<[]<>>[()()]]{[[]{}]{{}<>}}){(
((<[[([{<<{{{([]{}){<>{}}}({<><>}{{}{}})}<<<[]{}>(<>[])>([()<>])>}{<([(){}]({}[]))[({}<>)((){})]>[[<<
[[{<[((<[<{(([[]()][[][]]))}>]><[{([(<[][]>{(){}})<{{}[]}[{}{}]>])((<<{}()>[[][]]>{{()[]}((){})
{{{[(({{<<{({<{}<>><[]{}>}[<{}<>>({}[])])}>>{{{((<[]()>[(){}]))({<[][]>[<>[]]}[[<><>](()[])
<<((<({{{{<({({}()){<>()}}<[<>()]>){([[]<>]([]<>))[[()<>]]}>]{[({[{}()]{[][]}})({[[]()]{()()}}[(()[
[{<{{{[<[<<{{(()())({}{})}(<<><>>[[]<>])}><[<[<><>]<{}<>>>([[]()}{[][]})]>>[[{<[[]<>]<<>{}>><<(){}>{[]
<<[<<[[(([({[{()[]}{<>}]<(()())[[]()]>}<((<><>)<[]()>]{(<><>){(){}}}>)])({[<<([]{})<{}[]>>[[{}[]](<>
<[{{{<<<{<{({<{}[]>[<><>]})}<{([[]<>]([]<>))<[()<>]({}{})>}{{[{}()]({}<>)}}>>}<<((<{<><>}[()<>]>
({([{(((((([[<[]{}>((){})]<[()<>]<{}()>)]))[(<<([]()){[]<>}>[({}[])<{}{}>]><[[<>]{{}()}]<(()<>)[{}()]>>)]))<<
<[[<((([<[(((([][]){{}<>})(<<>()>{<>()}))<[[(){}]<{}()>]<{()<>}[<>]>>)<([<[]{}>[{}]]){<{{}{}}>(<<>()>{[]<>})}
({({(<(({([{{<<>()>}[<{}{}><{}{}>]}[(<[][]>[()()]){([]{})[<>[]]}]])})){<{(<(<{<>()}>)[[{<>()]<()[]
(<<<{{{{({[<{<()>[[]()]}<[<>]>>][{([()<>](()())){(<>())[<>[]]}}<{{()()}({}<>)}{[<><>]}>]}(<{[(()<>){()[]
<{[([({{[{({{[<>()]<<>{}>}([[]()]([]<>))}<<{<><>}>[([]<>)([]{})]>)(<[{[]<>}(<>[])]>[([()[]][{}()])[[{
[<<<(({<{{[<<([]<>)((){})>{(()()){<>{}}}>{[{[]()}<<>{}>]}]<<[{()<>}((){})}>[[(<>{})]]>}<{[<{<>{}}(())
[([({([<<{<[<<{}()>{<><>}>{<()[]>}]>([([[]()]([]{}))([[][]]{[]()})])}<{{(<[]{}>{()<>})<(<><>)<[
[({(<<{(<[[{<{<><>}<()[]>>}[<[[]{}][[][]]>(<<><>>{<>{}})]]<{{[<>]<()<>>}[([][])[<>()]]}<((()
<([[{(({[[<<((()[]){<>()})[<<><>]{()()}]>[[(()[]){{}<>}]{[()[]](()())}]>[(<[{}{}]<<>[]>><({}())>)({[()]})]]]}
[(<<<{(({({<[((){}}({}())]<<{}{}>((){})>>}<{<([]{})>({<>}<{}[]>)}[<<[]<>>[()()]><(()())[<>()]>]>){[{(
{<[[[{{<[{{{<<(){}>{[]<>}>[<(){}>({}[])]}<(<<>{}>)({()()})>}<([([][])<{}<>>]<{()[]}(<>())>)[([()<
(<<(<{[[(<{<<[()()]([]<>)>{<{}{}>([]{})}>}[([(<>{})[()()]][([]())[<>[]]]){([{}<>]{()[]})(<()[]>)}]>)]]
{<([[(<((<({{<(){}>([])}<[{}()][()<>]>}[[(()())]<[<>[]]((){})>])>([(<<[]><[][]>><({}{})[<>[]]>)])){{({[[[]<
[[[<<{([[{[(<<{}<>>>)]}<<<{{<>()}<<><>>}{[{}[]]{<>{}}}>>>][<{{{<[][]>[<>()]}[([]<>){{}<>}]}<({[](
({{({<<(<(([{{{}[]}([]<>)}{[()[]]([]<>)}]([{{}[]}<{}()>]{{{}<>}{<>[]}}))(<{<<>{}>}[{<>()}[<>[]]]>{(<()()>({}
{{<<{{({{[{<(<{}<>>){{{}<>}<()[]>}>}](<[[<{}[]><[][]>][(()())([]())]]({{{}{}}<(){}>}{{(){}
[{[<<{{[(<([[[{}{}]<()[]>]{((){})[{}()]}][(<[][]>{()})[<[]()>[[]{}]]>)>(<[<[[]()]<<>[]>>][[({}[])<
[[<<[{<<{{{<[{<><>}][{()[]}]>[(<<>{}><<>()))[[<><>]([]<>)]]}}}>[{<[{<([]{}){[]<>}>({(){}}{[]{}})}]([[(
[<([[<{<<([([(()())(()())])((((){})[[]{}]))][{[[[]()]]}]))>}>](<{({{(<{({}[]){[]{}}}<{{}[]}[{}[]]>
({<<{{<{(({[<([]())({}[])>(<<>[]><[]<>>)]{[([]<>){{}<>}][{{}()}<[]<>>]}})([({<[]()>{{}}]{<
<{{{{[<{[<([[({}{})<<>()>]{{()()}[{}{}]}][{[<><>](<>())}[[<><>][{}{}]]])(<({<>})>[<[{}{}]{
{[[[([[[{(<<{(<>[])[{}[]]}{<<>{}>(<>())}>({<()()>[{}[]]}(<{}[]>[[]<>]))>)}]{[{({(<{}{}>)<(()
{[(<{{[(<((<([<><>]{()[]})<{[]<>}(()<>)>><[(()())]<[()()][<>{}]>>))>)(<([[({[]<>}{()[]})({[]()}[{}()])]<<{
[{{<[{[[<<<<{(<>()){()()}}[({}())((){})]>((([]{})))><<[(<>[]){{}[]}][{{}{}}(()<>)]><[{[]{}}[[]{
[[<{<(<[([<[(<<><>>[{}<>])[<()()>{<>[]}]]{({{}()}{<>[]})({()<>}[{}<>])}>(([[{}{}]<(){}>]{{()()}
({<([[{{<<{<<[[]{}]((){})>[{<>()}[[]()]]>[[[[]()][[]{}]][<(){}>(<>())]]}(<{[{}()]{{}()}}{{{}
{{<<<(<{<[<[({{}{})<{}<>>)<{<><>}<()[]>>]{<(()())[{}]>}><<([<>{}]((){}))<[()[]]<<>()>>>(<{<>()}[<><>]>
<([{{{((((<[[<{}[]>{<><>}]<[()]<<>{}>>]<<<[][]>[[]<>]>[(()[]){()[]}]>>){[[([<>{}][<>{}])(([]
([(({{<<(({(({()}{{}()>))([(<>{})]<({}[]){<>()}>)}{<{{()()}<()<>>}<<[][]>(<>())>>})([[{[[]()]<<>
{[<(<{<({{({((<><>))[[[]{}]{[][]}]}<({{}<>}[[]<>]]<(()<>)<{}()>>>)}})[{{([{(<><>)[<>{}]}[[{}()]]]{[<
[<(<<[(({([[<<[][]><{}()>><{<><>>[<>[]]>]]((<(<>[]){<>{}}>{{()[]}(<>[])})))<((((()[])[()<>])))
""".strip().split('\n')
                            

#%% Part 1

"""
Stop at the first incorrect closing character on each corrupted line.

Did you know that syntax checkers actually have contests to see who can get the high score for syntax errors in a file? It's true! To calculate the syntax error score for a line, take the first illegal character on the line and look it up in the following table:

): 3 points.
]: 57 points.
}: 1197 points.
>: 25137 points.
In the above example, an illegal ) was found twice (2*3 = 6 points), an illegal ] was found once (57 points), an illegal } was found once (1197 points), and an illegal > was found once (25137 points). So, the total syntax error score for this file is 6+57+1197+25137 = 26397 points!

Find the first illegal character in each corrupted line of the navigation subsystem. What is the total syntax error score for those errors?
"""
from collections import defaultdict
import re

illegal_characters = ''

char_mapper = {')': '(', ']': '[', '}': '{', '>': '<'}
char_mapper2 = dict((v, k) for k, v in char_mapper.items())
points_mapper = {')': 3, ']': 57, '}': 1197, '>': 25137}

def is_corrupt(line):
    chunks_found = True
    while chunks_found:
        chunks_found = False
        for k, v in char_mapper2.items():
            if f"{k}{v}" in line:
                chunks_found = True
                line = line.replace(f"{k}{v}", '')
    r = re.findall(r'[\]\)\}\>]', line)
    if r:
        return True, r[0]
    else:
        return False, line
    
for line in _input:
    ic, r = is_corrupt(line)
    if ic:
        illegal_characters += r
        
points = 0
for char in illegal_characters:
    points += points_mapper[char]

print(points)

#%% Part 2
                          
"""
Now, discard the corrupted lines. The remaining lines are incomplete.

Incomplete lines don't have any incorrect characters - instead, they're missing some closing characters at the end of the line. To repair the navigation subsystem, you just need to figure out the sequence of closing characters that complete all open chunks in the line.

You can only use closing characters (), ], }, or >), and you must add them in the correct order so that only legal pairs are formed and all chunks end up closed.
                            
Did you know that autocomplete tools also have contests? It's true! 
The score is determined by considering the completion string character-by-character. 
Start with a total score of 0. 
Then, for each character, multiply the total score by 5 and then 
increase the total score by the point value given for the character in the following table:

): 1 point.
]: 2 points.
}: 3 points.
>: 4 points.

Find the completion string for each incomplete line, score the completion strings, 
and sort the scores. What is the middle score?
"""

scores = []

point_map2 = {')': 1, ']': 2, '}': 3, '>': 4}

for line in _input:
    ic, r = is_corrupt(line)
    if ic:
        continue
    completion = ''
    for c in r[::-1]:
        completion += char_mapper2[c]
    score = 0
    for c in completion:
        score = score * 5 + point_map2[c]
    scores.append(score)
    
scores = sorted(scores)
N = len(scores)
print(scores[int((N-1)/2)])
                            