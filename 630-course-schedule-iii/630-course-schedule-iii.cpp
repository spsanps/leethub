 bool comp(vector<int> a, vector<int> b) {
            return a[1] < b[1];            
        }

class Solution {
public:
    int scheduleCourse(vector<vector<int>>& courses) {
        
       
        
        sort(courses.begin(), courses.end(), comp);
        
        //for (auto & e1 : courses) {
        //    for ( auto & e2 : e1) {
        //        cout << e2 << " ";
        //    }
        //    cout << "\n";
        //}
        
        vector<int> q = {0};
        
        //make_heap(q.begin(), q.end());
        
        int tdur = 0;
        int dur, ld;
        for (auto & elem : courses) {
            dur = elem[0]; ld = elem[1];
            if (dur + tdur <= ld ) {
                q.push_back(dur);
                push_heap(q.begin(), q.end());
                tdur += dur;
            } else if (dur < q.front()) {
                tdur -= q.front() - dur;
                
                pop_heap(q.begin(), q.end());
                q.pop_back();
                q.push_back(dur);
                push_heap(q.begin(), q.end());
            }
            
            //for (auto & aele : q) {
            //    cout << aele << " ";
            //}
            //cout << "\n";
            //cout << tdur << "\n";
        }
        
        return q.size() - 1;
        
    }
};