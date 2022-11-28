
%{
/*Program to check if the number is octal or hexadecimal*/
%}
Oct [o][0-7]*
Hex [o][x|X][0-9A-F]*
%%
{Hex} printf("This is a hexadecimal number");
{Oct} printf("This is a octal number");
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