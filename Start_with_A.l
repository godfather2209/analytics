%{ 
/*Program to find identifiers starting with a/A using regular expressions*/
%}
%%
[a|A][0-9a-zA-Z]* printf("This is an identifier or keyword starting with letter 'a' or 'A'");
[0-9a-zA-Z]* printf("No match");
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