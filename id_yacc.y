%{
    #include<stdio.h>
    int valid=1;   
%}
%token letter

%%
start : letter s
s :   ; 
%%

int yyerror()
{
    valid=0;
    printf("\nIt is not an identifier!\n");
    return 0;
}

int main()
{
    printf("\nEnter the expression:\n");
    yyparse();
    if(valid)
    {
        printf("\nIt is Identifier!\n");
    }
}

