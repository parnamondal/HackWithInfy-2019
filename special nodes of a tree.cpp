 #include <bits/stdc++.h> 
using namespace std;
const size_t N = 1000000;
vector <bool> visited;
vector <int> color;
vector <int>queries;
vector <int>special;
//int result[100000];
vector <int> adj[N];
vector <int> result(N);
vector <int> r;

 
void dfs(int s) {
    visited[s] = true;
    for(int i = 0;i < adj[s].size();++i)    {
     if(visited[adj[s][i]] == false)
         dfs(adj[s][i]);
    }
}

void initialize() {
    for(int i = 0;i < 10;++i)
    visited.push_back(false) ;
    
     
}
void initialized() {
    for(int io = 0;io < 10;++io)
    special.push_back(0) ;
    // special[io]= 0;
}

int main() {
    initialize(); 
    initialized();
    int nodes,query,q,c, sum,edges, x,w,b,y, connectedComponents = 0;
    cin >> nodes;                       // Number of nodes
    for(int i = 0;i < nodes-1;++i) {
     cin >> x >> y;     
 // Undirected Graph 
     adj[x].push_back(y);                   // Edge from vertex x to vertex y
     adj[y].push_back(x);                   // Edge from vertex y to vertex x
    }
  for (int f= 0;f < nodes ;f++){
       cin >> b ;
        color.push_back(b); 
    }
    cin >> query ;
    for(int p = 0;p < query;p++) {
        cin >> w;
        queries.push_back(w);}
        int o =1;
for(int m=0;m <query;m++)
{  o=1;c=0;
  r.insert(r.begin(),queries[m]);
    r[0]=queries[m];
if(visited[queries[m]] == false)     {
         dfs(queries[m]);}
    for(int j = 0;j < adj[queries[m]].size();++j)
        {
        if(j == adj[queries[m]].size() - 1)
         r[o++]=adj[queries[m]][j];
      // r.insert(o++ ,adj[queries[m]][j]);
        else
             r[o++]=adj[queries[m]][j];
            // r.insert(o++,adj[queries[m]][j]);
}
 
if (special[r[0]-1] == 1 )  {
    c = result[queries[m-1]];
    }
    else {
        special[r[0]-1]=1 ;
        c+=1;
        for(int t=1;t<o;t++){
           if ( special[r[t]-1]==1 ){
               c+=result[r[t]];
           } //if - for loopcout <<c << "1" ;
           else {
               if ( (color[r[0]-1]) == (color[r[t]-1]) ){
               c+=1;
               special[r[t]-1]=1;
               }
           }//end of else 2 loop
           r[t]=0;
        }//for loop 
        r[0]=0;
    }//end of else loop
    int v = queries[m];
     if (c==1){
         int count =0;
     for (int y =0;y <nodes;y++){
         if (special[y]==1 )
         count++;
     } 
     result.at(v)=count;
     //result.insert(result.begin()+v,count);
       // result[queries[m]]= count;
        cout << count << endl ;
        
    }//end of if loop
    else {
        result.at(v)=c;
    // result.insert(result.begin()+v,c);
        //result[queries[m]]= c;
          cout <<c << endl ;
    }//end of else loop 
    c=0;v=0;
}
    return 0;
} // end of main loop
/*for (int po=0;po<o;po++){
  
    r[po]=0;   // MUST
} 
o = 1; // MUST*/
