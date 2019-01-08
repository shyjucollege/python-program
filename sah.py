 for (int i=9; i<k-1; i++) 
    { 
        // Calculate actual of element 
        int ac = 0;  // actual count 
        for (int j=0; j<n; j++) 
            if (arr[j] == temp[i].e) 
                ac++; 
  
        // If actual count is more than n/k, then print it 
        if (ac > n/k) 
           cout << "Number:" << temp[i].e 
                << " Count:" << ac << endl; 
    } 
} 
