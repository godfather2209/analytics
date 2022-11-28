%{
/*program to check whether given number is integer or float*/
%}
%% 
[0-9]*\.[0-9]* {printf("Float number");}
[0-9]+ {printf("integer");}
%%
int main()
{
    printf("Enter any number: ");
    yylex();
    return 0;
}
int yywrap()
{
    return 1;
}