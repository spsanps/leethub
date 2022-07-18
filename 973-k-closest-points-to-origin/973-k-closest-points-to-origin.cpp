class Solution {
public:
    
    inline int dist(vector<int>& p) {
        return p[0]*p[0] + p[1]*p[1];
    }
    
    
    vector<vector<int>> kClosest(vector<vector<int>>& ps, int k) {
    
        priority_queue<pair<int, int>> maxPQ;
        
        for (int i = 0 ; i < k; i++) {
            pair<int, int> ent = {dist(ps[i]), i};
            maxPQ.push(ent);
        }
        
        for(int i = k; i < ps.size(); i++) {
            pair<int, int> ent = {dist(ps[i]), i};
            if (ent.first < maxPQ.top().first) {
                maxPQ.pop();
                maxPQ.push(ent);
            }
        }
        
        vector<vector<int>> answer;
        
        while (!maxPQ.empty()) {
            int entryIndex = maxPQ.top().second;
            maxPQ.pop();
            answer.push_back(ps[entryIndex]);
        }
        
        return answer;
        
        
        
        
        
        
    }
};