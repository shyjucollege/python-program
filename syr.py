  if (j == k-1) 
        { 
            int l; 
              
            /* If there is position available in temp[], then place  
              arr[i] in the first available position and set count as 1*/
            for (l=0; l<k-1; l++) 
            { 
                if (temp[l].c == 0) 
                { 
                    temp[l].e = arr[i]; 
                    temp[l].c = 1; 
                    break; 
                } 
            } 
