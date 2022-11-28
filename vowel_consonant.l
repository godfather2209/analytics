%{
/*lex program to find number of vowels and consonants*/
int vowels_count=0;
int consonants_count=0;
char vowels[100];
char consonants[100];
int i=0;
%}
%%
[aeiouAEIOU] {vowels_count++; vowels[vowels_count-1]=yytext[yyleng-1];}
[a-zA-Z] {consonants_count++; consonants[consonants_count-1]=yytext[yyleng-1];}
"\n" return 0;
%%
int main()
{
printf("Enter any string: ");
yylex();
printf("Vowels count: %d\n", vowels_count);
printf("consonants count: %d\n", consonants_count);
printf("Vowels present are: ");
for (i=0; i<vowels_count; i++)
printf("%c", vowels[i]);
printf("\nConsonants present are: ");
for (i=0; i<consonants_count; i++)
printf("%c", consonants[i]);
return 0;
}
int yywrap()
{
return 1;
}