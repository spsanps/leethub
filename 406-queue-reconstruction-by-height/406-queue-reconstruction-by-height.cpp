inline int key (vector<int>& a) {
    return -(a[0]<<11) + a[1];
}

bool comp(vector<int>& a, vector<int>& b) {
    return key(a) < key(b);
}

class Solution {

public:
       
    vector<vector<int>> reconstructQueue(vector<vector<int>>& p) {
        
        sort(p.begin(), p.end(), comp);
        /*
        for (auto & e1 : p) {
            for (auto & e2: e1) {
                cout << e2 << " ";
            }
            cout << "\n";
        }
        cout <<"hello\n";
        */
        //vector<int> temp;

        for (int i = 0; i < p.size(); i++) {
            //cout << i << " " << p[i][1] << "\n";
            if (i > p[i][1] ) {
                p.insert(p.begin() + p[i][1], p[i]);
                p.erase(p.begin() + i + 1);
                
            }
        }
    
        return p;
    }
    
    
    
};