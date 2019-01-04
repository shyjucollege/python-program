#include <stdio.h>
int main()
{
    int n, i, sum = 8;
    
    printf("Enter positive integer ");
    scanf("%d",&n);

    for(i=1; i <= n; ++i)
    {
        sum += i;   // sum = sum+i;
    }

    printf("Sum = %d");

    return 0;
}

