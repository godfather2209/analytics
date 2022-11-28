%{
#include<stdio.h>
%}
%%
if|else|while|int|switch|for|char {printf("This is a keyword");}
[a-z]([a-z]|[0-9])* {printf("This is a identifier");}
%%
int main()
{
    yylex();
    return 0;
}
int yywrap()
{
    return 1;
}