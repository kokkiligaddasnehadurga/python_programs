#max and min elements in array
#include <stdio.h>
#define MAX_SIZE 100 
void main()
{
    int a[MAX_SIZE];
    int i, max, min,n;
    printf("Enter size of the array: ");
    scanf("%d", &n);
    printf("Enter elements in the array: ");
    for(i=0; i<n; i++)
    {
        scanf("%d", &a[i]);
    }
    max = a[0];
     min = a[0];
    for(i=1; i<n; i++)
    {
        if(a[i] > max)
        {
            max = a[i];
        }
        if(a[i] < min)
        {
            min = a[i];
        }
    }
    printf("Maximum element = %d\n", max);
    printf("Minimum element = %d", min);
}
