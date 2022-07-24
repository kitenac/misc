
# Строки в python3 - массивы символов из таблицы Unicode. Не путать понятие кодировки(биты --> десят.числа) и таблицы символов(дес. число ---> символ).
#  Unicode - очень большая таблица(8 БАЙТ ==> (8*8)^8 символов), в ней даже не все символы задействованы.
#  Поэтому в зависимости от задачи символ Unicode весит от 1(совпадает с ASCII) - до 8 байт( смайлики, кит. алфавит, иврит ....) 



print(f'''\n  {chr(9773)*10} {chr(9794)*5} {chr(9895)*3}
    {chr(9749)} {chr(8419)}  {chr(8987)} {chr(8986)}  {chr(9208)} {chr(9757)} {chr(9748)}
{chr(9775)} {chr(9855)} {chr(9889)} {chr(9935)} {chr(9939)} {chr(9924)} {chr(9940)}
{chr(9811)} {chr(9803)} {chr(9808)} {chr(9804)} {chr(9809)}
{chr(9898)} {chr(9899)} {chr(11042)} {chr(11044)} {chr(11036)}
{chr(9961)} {chr(9962)} {chr(9968)}


Emoji 
{chr(9977)} {chr(9994)} {chr(9995)} {chr(9996)} {chr(9997)} {chr(10024)}
{chr(10060)} {chr(10067)} {chr(10071)} {chr(10133)} {chr(10134)} {chr(10135)}
{chr(11088)} {chr(11093)} 



{chr(9872)} {chr(9873)} {chr(9892)} {chr(9890)} {chr(9891)}
{chr(9760)} {chr(9762)}  {chr(9763)} {chr(9774)}
{chr(9785)} {chr(9786)} {chr(9787)} {chr(9788)} {chr(9789)}
{chr(9814)} {chr(9816)} {chr(9825)} {chr(9829)} {chr(9832)}
{chr(9834)} {chr(9835)} 


9472 - 9639 - are usefull to drawing,for ex: {chr(9604)} {chr(9617)} {chr(9618)} {chr(9619)}
10136-10174 - arrows
10229-10239 - more arrows
10496-10612 - arrows again, but more complicated
10241-10495 - dots for blind people
10764-10780 - integrals

{chr(10239)}  
            {chr(1161)}             {chr(990)} {chr(991)}    {chr(886)}
            {chr(761)} {chr(762)}    {chr(661)}      {chr(990)}
            {chr(763)} {chr(764)}    {chr(176)}      {chr(171)}      {chr(7931)}
  {chr(1645)}   {chr(2017)}  {chr(4277)}  {chr(4416)}  {chr(4485)}
 {chr(5129)}   {chr(5514)}  {chr(5765)}    {chr(5784)}  {chr(5781)} {chr(7425)} 
  {chr(8224)}  {chr(8226)}  {chr(8258)}  {chr(8253)}   
    {chr(8284)}   {chr(8287)} {chr(8265)}  {chr(8578)}
  {chr(8627)}  {chr(12295)} {chr(42572)}  {chr(42604)} {chr(42606)}

Math: {chr(8704)}  {chr(8754)} {chr(8853)}
  {chr(9127)}
  {chr(9128)}
  {chr(9129)}


Chemistry: {chr(9004)}, {chr(9187)}

 {chr(8413)}    {chr(8414)}   {chr(8415)}   {chr(8420)}  {chr(9022)}
 {chr(8466)} {chr(8461)} {chr(8499)} {chr(8512)}   {chr(9036)} {chr(9095)}
   {chr(8889)}   {chr(8886)} {chr(8920)} {chr(8984)} {chr(9096)} {chr(9098)}
  {chr(9453)} {chr(9450)}  {chr(9688)} {chr(9841)} {chr(9884)} {chr(9904)}
{chr(9909)} {chr(9883)} {chr(9901)} {chr(9986)} {chr(9992)}
{chr(10007)} {chr(10004)} {chr(10026)} {chr(10016)} {chr(10014)} {chr(10017)}
{chr(10038)} {chr(10052)} {chr(10058)}

                                                                 ''')






magic_a = "      " + chr(1161)*30  # i don`t know why, but if to try print 1161/1160 symbols in multiple - they wanish 
magic_b = "      " + chr(1160)*30  #  but if to add smth befoore it it works \_(O_o)_/



print(magic_a*7 + ''' 
     Look at some amazing symbols from Unicode abowe!!! \n''', magic_b*7, sep = '', end = '\n'*5)

print("Type start number in Unicode table to show", end = '\n: ')


i = int(input())
print("Press any key to start")
while input() != 'q': 
 for j in range(30):
  if 157<=i+j<=159: 
   print("This sybol terminates program")
   continue
  print(f'{i + j}|     {chr(i + j)} ')
 
 print("Press any key to output next 30 charectors in Unicode table and 'q' to quit")
 i += j + 1



#print(chr(156))

