---
title: 动态规划DP相关（内含闫氏分析法的讲解与相关习题  
date: 2023-03-28 16:54  
tags: [C++,dp]  
source: https://blog.csdn.net/SHIE_Ww/article/details/129701139  
---
## 一. 动态规划的分析角度

-   动态规划是不断决策求最优解的过程

### 状态表示：考虑问题有几维需要考虑

-   集合：每个状态都是一个集合==>我们要考虑状态`f(i,j)`表示的是哪一个集合
    -   集合条件：①只从前i个物品中选；②总体积≤j
-   属性：集合存的其实是一个数，即属于集合的某种属性。
    -   属性一般有三种：最大值；最小值；元素的数量

### 状态计算：如何一步步把每个状态计算出来

-   集合划分
    -   ①不重（不一定）
    -   ②不漏

### Dp优化：一般是对动态规划的代码或计算方程，做一个等价变形

-   要先把基本朴素的写法写出来后，再对Dp考虑做优化：二维→一维

___

## 二. [背包问题]

-   背包问题的特点：有N件物品和一个容量为V的背包，每件物品有各自的价值。要求在有限的背包容量下，装入的物品总价值最大。

### 1\. 01背包

-   特点：每件物品最多只用一次
-   体悟：一个人的价值再大
    -   ①首先不能狮子大开口要得超出他人力所能及的范围，否则就是庙小容不得大佛，只能另请高明。
    -   ②其次，要和他人合作达成最大产能才能被留下。
    -   ③总结：被留下只能a.请你的代价不大于其他多人总和；b.你带来的价值不小于他人带来的价值；c.公司留有余力，允许你的加入，并能因为你和他人合作获得更大产值。
        -   c的出路相对合理
        -   a和b的平衡很重要，高价值的人不该以低要求来抢下一层的人的饭碗，导致恶性低效的竞争；低价值的人也不能过分高判自己，可先找当前阶段相匹配的岗位，而后提高价值。

##### 01背包思考分析

-   状态表示：背包问题有两维（重量，价值）需要考虑==> `f(i,j)`
    
    -   集合：对于背包问题，集合表示的是所有选法的一个集合
        -   集合条件：①只从前i个物品中选；②总体积≤j
    -   属性：背包问题属性存的就是集合里最大值
-   状态计算：背包问题中，状态重量为1时最大价值是多少？为2、3……n时各为多少
    
    -   从`f[0][0]=0`开始决策(有N件物品,则需N次决策),每次对第i件物品的决策,`f[i][j]=0`不断由之前状态更新而来
    -   对于背包问题求`f(i,j)`，即从1到i，总体积不超过j中选总价值最大的 ==> 可分为两部分:
        -   ①不含i的总价值最大`f(i-1,j)` ==> 一定存在
        -   ②含i的总价值最大`f(i-1,j-vi)+wi` ==> 未必存在（当i>j时，此就为空集）
        -   \==> 最终`f(i,j)=max( f(i-1,j), f(i-1,j-vi)+wi )`
-   Dp优化：
    
    -   背包问题状态转移方程f(i)这层在转移的时候只用到了f(i-1)==>可用滚动数组来做。
        -   滚动数组：在计算某个状态时，只保留该状态的前一个状态和当前状态，而将之前的状态全部丢弃。==> 从而将空间复杂度从O(nm),降到O(m)
    -   并且不论是否含i，都是＜j的 ==>故可用一维来算

##### 01背包例题：[2\. 01背包问题 - AcWing题库]

-   朴素解法:二维图解
    
    -   ![![[Pasted image 20230228224103.png]]][fig1]
-   朴素解法:二维代码分析
    
    -   分析点①：依次输入第i件物品的体积和价值
        -   但由于每轮更新的是“ 允许第i个物品被放入后，不同j值下的最高价值（即以每个物品为第一维`dp[i][]`）”，所以更新当前的`dp[i][]`时并用不到第i个物品之后的物品 ==> 故可以每输入一个物品属性后就更新一下dp，节省了一次for循环。
        -   虽有一定优化，但优化程度不大，可根据可读性做取舍。
    -   分析点②：若仅仅第i个物品就超过了背包的最大容积，则意味着不能装它进去 ==> 其价值等于前i-1个物品讨论的最高价值度
        -   `dp[i][j]`：表示只从前i个物品中选,且总体积≤j的最高价值。
    -   分析点③：状态转移方程 `dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i]]+v[i]);`
        -   第i个物品小于背包的最大容积，仅意味着它有机会装进去，但是否选它装进去，还需要进一步max比较它能否带来更高价值（如果）。
        -   `dp[i-1][j]`：不选第i个物品加入的最高价值度
        -   `dp[i-1][j-w[i]]+v[i]`:选第i个物品加入
            -   为什么不直接`dp[i-1][j]+v[i]`？
                -   因为`w[i]≤j`仅表示其具有最基本能放进包的条件，但`dp[i-1][j]`最优的情况所占据的体积+`w[i]`后，可能已超出了j的体积.
                -   🔺`dp[i-1][j]`最优的情况是指：能放第i-1件物品**讨论的最优结果**，未必是放进了i-1件物品，因为第i-1件物品也未必放得进去。
            -   故`dp[i-1][j-w[i]]`表留出`w[i]`空位后的最优情况，在此基础上才能`+v[i]`
        -   为什么要max比较一下，不直接`dp[i][j]=dp[i-1][j-w[i]]+v[i];`呢？
            -   由于`dp[i-1][j]`和`dp[i-1][j-w[i]]`的大小关系未知，不能因后者多加了`v[i]`部分，就判定后者大。
            -   故需要一层max来看看，加入了当前第i项的价值并牺牲当前第i项的容积后，是否能取得更大价值。
    -   为什么以`j`和`w[i]`作为`dp[i][j]`的分水岭呢？
        -   因为`w[i] ≤ j`是考虑是否当前项有机会参与最高价值判定的最基本条件，若不满足（即`w[i] ＞ j`）则不论其价值多高，都白谈，小庙请不起大佛。
        -   并且输入物品并非按照体积从小到大的顺序排列，故不能检测到谁不满足小于j的条件就停止后面物品的参评。并且层都是应用上层的数据，所以即使当前i体积太大，也要将i-1层的数据更新到i层的数据
-   朴素解法:二维具体代码
    

```
#include<iostream>
#include<algorithm>
using namespace std;
const int N =1010;

int dp[N][N];//dp[i][j]:j体积下前i个物品的讨论后的最大价值
int w[N],v[N];//w:weight重量;v:value价值
int n,m;//背包允许最多放入n件物品,最后求解总重不超m情况的最高价值

int main()
{
    cin>>n>>m;
    
    // 依次读入第i件物品的体积和价值 ---分析点①
    // for(int i = 1; i <= n; i++) 
    // cin >> w[i] >> v[i];

    for(int i=1;i<=n;i++){
        cin>>w[i]>>v[i];//分析点①
        for(int j=1;j<=m;j++){//二维：正序/逆序都可以
            //全转第i个物品都装不下
            if(w[i]>j){ 
                dp[i][j]=dp[i-1][j];//分析点②
            }else{//虽能装，但需进行决策是否选择第i个物品会有更大价值
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i]]+v[i]);//分析点③
            }
        }
    }
    cout<<dp[n][m];
    return 0;
}
```

-   优化解法:一维代码分析
    
    -   一维优化详解参考：[2\. 01背包问题 - AcWing题库]
        
    -   为什么能用一维数组代替二维数组？
        
        -   ![![[Pasted image 20230228224358.png]]][fig2]
    -   分析点①：此处的物件属性读入，优化到双层for循环中的首层中优化程度近乎没有。
        
    -   分析点②：为什么要逆序更新？
        
        -   ![![[Pasted image 20230228224439.png]]][fig3]
-   优化解法:一维具体代码
    

```
#include <iostream>
using namespace std;

const int N = 1010;

int n, m;
int v[N], w[N];//v价值；w重量
int dp[N];

int main() {
    cin >> n >> m;
    //依次读入第i件物品的体积和价值 ---分析点①
    for(int i = 1; i <= n; i++) 
    cin >> w[i] >> v[i];
    
    for(int i = 1; i <= n; i++) 
        for(int j = m; j >= v[i]; j--) //分析点②
            dp[j] = max(dp[j], dp[j-w[i]]+v[i]);
            
    cout << dp[m] << endl;
return 0;    
}
```

### 2\. 完全背包

-   要求：现有 N 种物品和一个最多能承重 M 的背包，每种物品都有无限个，第 i 种物品的重量是 wi ，价值是 vi.在背包能承受的范围内，试问将哪些物品装入背包后可使总价值最大，求这个最大价值。
-   特点：每件物品有无限个
-   完全背包和01背包区别：
    -   01背包问题循环体积的时候，从大到小 ==> `f[i,j] = Max(f[i-1,j],f[i-1,j-v]+w`
    -   完全背包问题是从小到大循环 ==> `f[i,j] = Max(f[i-1,j],f[i,j-v]+w`

##### 完全背包思考分析

-   状态表示及计算,完全背包和[01背包问题]相同.
    
-   状态表示： `dp[i][j]`重量+价值
    
    -   集合：所有只考虑前i个物品,且总体积不大于j的所有选法.
    -   属性：集合中的最大值
-   状态计算：集合的划分
    
    -   状态方程的计算:`f[i,j] = max(f[i-1,j],f[i-1,j-v[i]*k]+w[i]*k)`
    -   k=0时,即未加入当前第i个物品,则结果即为f(i-1,j)
    -   对于当前第i个物品选入的计算
        -   ①去掉k个物品i的重量
        -   ②求max
        -   ③加回k个物品i的价值
-   Dp优化：
    
    -   和01背包区别：01背包问题循环体积的时候，从大到小；完全背包问题是从小(`j=v[i]`)到大(`j=m`)循环

##### 完全背包例题：[3\. 完全背包问题 - AcWing题库]

-   朴素解法:二维代码分析
    -   `dp[i][j]`: 在背包承重为j的前提下,从前i种物品中选能够得到的最大价值.
    -   分析点①:当k为0时,表示并不选用当前第i个物品,故k为0是有意义的,所以k必须从0开始.
    -   分析点②:
        -   对于01背包,max只需比较装进第i个物品和没装第i个物品的仅两者价值高低;
            -   01背包也可以选择用k循环,但k只有0(没选)和1(即使选,也仅能选1个)的情况,故用if-else更方便.
        -   对于完全背包,max需要比较没装第i个物品(1种情况)/装进第i个物品(后者可能装进k个,则有k种情况) --> 意味着要在1+k种情况中得最高价值
            -   虽然max仅能对两者进行比较,但其实k=0第一轮比较中(初始化`dp[i][j]=0`和`dp[i-1][j]`),总会先留下没装进第i个物品的情况.
            -   而后若k有机会被放下,甚至有机会放入多个,才会继续一一比较.
            -   最后总能保证`dp[i][j]`留下的都是最高价值.
-   朴素解法:二维具体代码
    -   无法通过,效率低,会导致超时TLE(Time Limit Exceeded)

```
#include<iostream>
using namespace std;

const int N = 1010;

int n, m;
int dp[N][N], v[N], w[N];

int main(){
    cin >> n >> m;
    //读入各物品的体积和价值
    for(int i = 1; i <= n; i ++ )
        cin >> w[i] >> v[i];

    for(int i = 1; i <= n; i ++ )
        for(int j = 0; j <= m; j ++ )
            for(int k = 0; k * w[i] <= j; k ++ )//分析点①
                dp[i][j] = max(dp[i][j], dp[i - 1][j - k * w[i]] + k * v[i]);//分析点②
    cout << dp[n][m] << endl;
    return 0;
}
```

-   优化解法:一维具体代码
    -   优化策略:将第三重k的循环优化掉.
        
        -   ![![[Pasted image 20230301201819.png]]][fig4]
    -   模拟过程图解:![![[Pasted image 20230301195644.png]]][fig5]
        
    -   分析点①: 01背包问题循环体积的时候，从大到小；完全背包问题是从小到大循环.
        
        -   为什么完全背包问题不用逆序? 因为在01背包中逆序是为了保证更新当前状态时，用到的状态是上一轮的状态，保证每个物品只被选中1次或0次;而对于完全背包问题，每个物品可以取任意多次，所以不再强求用上一轮的状态(因为即使用到的是本轮刚更新过的状态, 则表放了多个本轮物品)

```
#include<iostream>
using namespace std;

const int N = 1010;

int n, m;
int dp[N], v[N], w[N];

int main(){
    cin >> n >> m;
    //读入各物品的体积和价值
    for(int i = 1; i <= n; i ++ )
        cin >> w[i] >> v[i];

    for(int i = 1; i <= n; i ++ )
        for(int j = w[i]; j <= m; j ++ )//分析点①
            dp[j] = max(dp[j], dp[j - w[i]] + v[i]);
    cout << dp[m] << endl;
    return 0;
}
```

-   进一步细节方面的小优化:
    -   ①遍历每一轮i时，用到的`v[i]和w[i]`只来自本轮的输入，并且之后不会再用到，因此不用创建数组来存这两个值。
    -   ②可以边输入,边更新每轮的i (🔺注意for循环执行多条语句,就需要加大括号`{}`,经常忘记,要多注意)

```
#include<iostream>
using namespace std;
const int N = 1010;
int n,m,w,v;
int dp[N];

int main(){
    cin >> n >> m;
    for(int i = 1; i <= n; i ++ ){
        cin>>w>>v;
        for(int j = w; j <= m; j ++ )
            dp[j] = max(dp[j], dp[j - w] + v);
    }
    cout << dp[m] << endl;
    return 0;
}
```

### 3.多重背包

-   每件物品规定有限个（有各自的个数限制）==> 第i种物品最多有si件，每件体积是wi，价值是vi

##### 多重背包思考分析

-   状态表示：`f[i,j]`
    
    -   集合：所有只从前i个物品中选，并且总体积不超过j的选法
    -   属性：最大值（集合中所有选法对应的总价值的最大值）
-   状态计算：集合划分的过程
    
    -   集合划分依据：根据第i个物品有多少个来划分.含0个、含1个……含k个
    -   `f[i,j] = max(f[i - 1][j - v[i] * k] + w[i] * k; k = 0, 1, 2, ..., s[i]`（类似朴素版本的完全背包问题）
-   Dp优化：
    
    -   优化思路①：通过`f[i,j-v]`求出`f[i,j]` ==> 不可取，原因如下图
        
        -   ![![[Pasted image 20230301211605.png]]][fig6]
    -   优化思路②：二进制的优化 方式
        
    -   优化思路③：将多重背包拆成01背包
        
        -   当si=1时，相当于01背包中一件物品
        -   当si>1时，相当于01背包中多个一件物品 ==> 拆分

##### 多重背包例题1（数据量小）： [4\. 多重背包问题 I - AcWing题库]

-   对于该题数据量小，采用朴素和拆分成01背包优化的共三种写法，效率都差不多
    -   朴素看起来还好理解一点，但只要数据量大一点1010，不论是朴素还是拆分成01背包都过不了 ==> 只能采用二进制优化\[\[5.动态规划#多重背包例题2（数据量大）： 5 多重背包问题 II - AcWing题库 https www acwing com problem content 5\]\]
-   朴素版：代码分析
    -   分析点①：与完全背包相比较，对于两者的朴素版，多重背包在k循环的条件下，多了si的限制
-   朴素版：具体代码

```
#include <iostream>
using namespace std;
const int N =110;
int n,m;
int v[N],w[N],s[N];//v,w,s;
int dp[N][N];

int main()
{
    cin>>n>>m;
    
    for(int i = 1; i <= n; i ++ )
        cin >> w[i] >> v[i] >> s[i];
        
    for(int i = 1; i <= n; i ++ )
    for(int j = 0; j <= m; j ++ )
    for(int k = 0; k <= s[i] && k*w[i]<=j; k ++ )//分析点①
    dp[i][j] = max(dp[i][j],dp[i-1][j-w[i]*k] + v[i] * k);

    cout<<dp[n][m];
    
    return 0;
}
```

-   优化3：多重背包拆成01背包解决
    -   写法①和②效率都差不多

```
//写法① 好理解
#include <iostream>
using namespace std;
const int N =10010;//100*100+10
int n,m,idx,v,w,s;
int vv[N],ww[N];//用于存储拆分后的价值v和体积w；
int dp[N];

int main()
{
    cin>>n>>m;
    
    while(n--)
    {
        cin>>w>>v>>s;
        while(s--)
        {
            ww[++idx]=w;
            vv[idx]=v;
        }//死拆，把多重背包拆成01背包
    }
    //拆分后的总数即idx
    for(int i=1;i<=idx;i++)
    for(int j=m;j>=ww[i];j--)
    dp[j]=max(dp[j-ww[i]]+vv[i],dp[j]);//套01背包的板子
    
    cout<<dp[m]<<endl;
    return 0;
}
```

```
//写法② 省事（其实和写法①相同思路）
#include <iostream>
using namespace std;
const int N =10010;//100*100+10
int n,m,v,w,s;
int dp[N];

int main()
{
    cin>>n>>m;
    while(n--)
    {
        cin>>w>>v>>s;
        //表示能走s次01背包的多重一个物品
        while(s--){
for(int j=m;j>=w;j--)
dp[j]=max(dp[j-w]+v,dp[j]);//套01背包的板子
        }
    }
    
    cout<<dp[m]<<endl;
    return 0;
}
```

##### 多重背包例题2（数据量大）： [5\. 多重背包问题 II - AcWing题库]

-   对于数据量大的多重背包问题，需要采取二进制优化的解法
    
-   思路分析：
    
    -   为什么不能直接拆分成01背包问题？
        -   若直接遍历转化为01背包问题，每次都拿一个来问“取了好还是不取好”，那根据数据范围，时间复杂度是O(n³)，即10<sup>9</sup>，必会TLE
    -   理解二进制优化思维的三个前置知识
        -   ①多重转01背包的思路：逐一判断每件物品是取了好还是不取好
        -   ②任意一个实数可以由二进制数来表示（即2<sup>0</sup>~2<sup>k</sup>其中一项或几项的和）
        -   ③多重背包问的是：每件物品取多少件可以获得最大价值。
    -   举例理解二进制优化思维：要求在一堆苹果选出n个苹果。
        -   朴素改01背包：一个一个地去选，选够n个苹果就停止。==> n次
        -   二进制优化：现有一堆苹果和10个箱子，选出n个苹果。将这一堆苹果分别按照1(2<sup>0),2(2</sup>1),4,8,16，……，512(2^9)分到十个箱子中，由于任何一个数字`x∈[0,1023](第11个箱子才会取到1024)`，所以任何一个数字都可以从这10个箱子里的苹果数量表示出来（根据前置知识②），并且这样选择的次数 ≤10次
        -   具体例子：比如要拿1001次苹果
            -   朴素：拿1001次
            -   二进制思维：最多尝试10次（分别尝试装512、256、128、64、32、16、8、4、2、1），最后可得出结果拿7个箱子最优（分别尝试装512、256、128、64、32、8、1）
    -   参考博文：[AcWing 5. 二进制优化，它为什么正确，为什么合理，凭什么可以这样分？ - AcWing]
-   代码分析
    
    -   分析点①：开`N*logS`大小的解释
        
        -   假设共有1000个物品（N≤1000），每个物品拆分成log2000个物品（因为每个物品出现2000次（si≤2000）），所以要开到`1000*log2000`大小（log1000=10，log2000(log2+log1000)向上取整是11，所以最多开到`1000*11`即11000，开到15000保险一点）
            
            -   log2000是以2为底分的,类似二叉树每层也都是2的次幂
        -   也可理解作：将重复的s个物品，打包成log s个新的物品组，用它们可以凑出0~s的任何一个数 ==> 时间复杂度O(s)优化成O(log(s))![![[Pasted image 20230301223150.png]]][fig7]
            
        -   为什么拆分后的能保证1~s件都能拼凑出呢？![![[Pasted image 20230302171202.png]]][fig8]
            
    -   分析点②：dp数组中存的是背包可容纳最大重量，即最大为V（代码中即m），题目表示V∈( 0, 2000 \]。因此dp初始化M=2010大小。
        
    -   分析点③：为什么还要判断`if(s>0)`呢？
        
        -   因为有可能本该剩下的最后一组数属于2的次幂数，即此时s=0，而当s=0则不必再开一组了。
        -   而s>0，则表示还剩余下的一组数，s即为改组的物件个数
    -   分析点④：![![[Pasted image 20230302170112.png]]][fig9]
        
    -   分析点⑤：各多重背包分组的第一组中物品个数总是1(即2º=1)开始（不论s=1或s>1）
        
-   具体代码
    

```
#include<iostream>
using namespace std;
const int N = 15000, M = 2010;//N:dp数组；M:重量、价值数组；分析点①

int n, m;
int v[N], w[N]; 
int dp[M]; //分析点②

int main()
{
    cin >> n >> m;//n物品种类；m背包容积
    int cnt = 0; //记录分组的组别
    for(int i = 1;i <= n;i ++)
    {
        int a,b,s;
        cin >> a >> b >> s;// 第i个物品的单个体积/单个价值/数量
        int k = 1; // 分析点⑤
        while(k<=s)
        {
            cnt ++ ; //组别先增加
            //分析点④
            w[cnt] = a * k ; // 整体体积 
            v[cnt] = b * k ; // 整体价值
            s -= k; // s要减小
            k *= 2; // 组别里的个数增加（2¹，2²，2³……）
        }
        //剩余的一组
        if(s>0)//分析点③
        {
            cnt ++ ;
            w[cnt] = a*s; 
            v[cnt] = b*s;
        }
    }

    n = cnt ; //枚举次数由个数变成组别数：此时的n表示表示将多重背包二进制分组后（cnt），最后的所有组数。
    //01背包一维优化
    for(int i = 1;i <= n ;i ++)
        for(int j = m ;j >= w[i];j --)
            dp[j] = max(dp[j],dp[j-w[i]] + v[i]);

    cout << dp[m] << endl;
    return 0;
}
```

### 4.分组背包

-   有N个类的大组（每组下有不同的物品），每组中只能选一个

##### 分组背包思考分析

-   和多重背包问题的思考方式是一样的
    
-   状态表示
    
    -   集合：只从前i组物品中选，且总体积不大于j的所有选法
    -   属性：max
-   状态计算
    
    -   `dp[j]=max(dp[j],dp[j-w[k]]+v[k]);`
-   Dp优化
    
    -   若转移的时候用的是上一层的状态，就从大到小来枚举体积（能保证在计算体积的时候，所用到的体积还没被计算过，所以存的是上一层的状态）
    -   若用的是本层的状态，就从小到大来枚举体积

##### 分组背包例题：[2\. 01背包问题 - AcWing题库]

-   ![![[Pasted image 20230302211823.png]]][fig10]
    
-   代码分析
    
    -   分析点①为什么要先枚举体积再枚举大组中小组物品呢?
        -   因为如果先枚举小组的物品,再枚举体积,相当于在每个大组别下进行01背包,就会导致dp数组中保留的可能是,一个大组中多选物品的可能
        -   而题目要求的是,每个大组中,只能选一个物品.
        -   而"先枚举体积,再枚举大组中小组物品",就能保证在最外层大组别循环切换后,内部的小物品选择时都是建立在,上一层大组别中只选了一样物品的基础上,符合题意.
-   具体代码
    

```
#include<iostream>
using namespace std;

const int N=110;
int dp[N],v[N],w[N];
int n,m;

int main()
{
    scanf("%d%d",&n,&m);//n物品大组;m背包容积
    for(int i=0;i<n;i++)//最外层循环大分组
    {
        int s;
        scanf("%d",&s); //输入当前大组里的物品数

        for(int j=0;j<s;j++) scanf("%d%d",&w[j],&v[j]); //输入各物品的体积和价值

        //分析点①
        //处理大分组里各个物品,其中dp[j]使用的是上一个大分组后最优的情况
        for(int j=m;j>=0;j--) //枚举所有体积
            for(int k=0;k<s;k++) //枚举所有选择
                if(j>=w[k]) //体积j需不小于当前物品体积,否则放不下
                    dp[j]=max(dp[j],dp[j-w[k]]+v[k]);//不选/选当前物品的情况
    }
    printf("%d",dp[m]);
    return 0;
}
```

___

## 三. 线性DP

-   🔺若有涉及到`f[i-1]`的,就习惯`i从1`开始取,保证最小`f[i-1]=f[0]`不会越界; 若没有涉及到,就`i可从0`开始取.
-   时间复杂度: `状态数量×每个状态转移的计算量`
-   线性DP的动态规划:

### 例题1:数字三角形

-   [898\. 数字三角形 - AcWing题库]
-   线性DP状态分析
    -   状态表示: `f[i,j]`
        -   集合:所有从起点,走到(i,j)的路径
        -   属性:max
    -   状态计算:
        -   ![在这里插入图片描述][fig11]
            
        -   思路①：往下走==>考虑边界问题，对`f[][]`均初始化为极小值,且不能越界
            
            -   从左上`(i-1,j-1)`走来，即f<sub>i-1,j-1</sub> + a<sub>i,j</sub>
            -   从右上`(i-1,j)`走来，即f<sub>i-1,j</sub> + a<sub>i,j</sub>
            -   故状态转移方程：f<sub>i,j</sub> =max{ f<sub>i-1,j-1</sub> ，f<sub>i-1,j</sub> }+ a<sub>i,j</sub>
        -   思路②：往上爬==>不用考虑边界问题
            
            -   从左下`(i+1,j+1)`走来，即f<sub>i+1,j+1</sub> + a<sub>i,j</sub>
            -   从右下`(i+1,j)`走来，即f<sub>i+1,j</sub> + a<sub>i,j</sub>
            -   故状态转移方程：f<sub>i,j</sub> =max{ f<sub>i+1,j</sub> ，f<sub>i+1,j+1</sub> }+ a<sub>i,j</sub>
                -   答案即 `f[1][1]`
-   代码分析:
    -   ![![[Pasted image 20230302211708.png]]][fig12]
    -   本题思路并非贪心（即并非只二选一选两者中大的走），而是dp遍历三角形每个位置上的数字，记录走到该位置上最大的和
    -   分析点①：为什么往下思路中，要初始化f数组为负无穷大？
        -   f数组未初始化默认为0，且测试数据中路径中含负值。
        -   若不初始化为负无穷大，则访问到三角形外的区域时，会导致最长距离计算错误
    -   分析点②：为什么往上思路中，要先用a数组最底层初始化f最底层呢？
        -   因为a数组最底层是最初的数据基础，f数组要依靠最后一层进行第一轮的路径求和
-   具体代码:

```
//思路①：向下走
#include <iostream>

using namespace std;
const int N = 510,INF = 1e9;
int n;
int a[N][N],f[N][N];

int main () {
//数据输入
    scanf("%d",&n);
    for (int i = 1;i <= n;i++) {
        for (int j = 1;j <= i;j++) 
            scanf("%d",&a[i][j]);
    }

//初始化f数组为负无穷大 -- 分析点①
    for (int i = 0;i <= n;i++) {
        for (int j = 0;j <= i + 1;j++) {
            f[i][j] = -INF;
        }
    }
    
    //从a[1][1]开始遍历每个位置找最大和的路径
    f[1][1] = a[1][1];
    for (int i = 2;i <= n;i++) {
        for (int j = 1;j <= i;j++) {
            f[i][j] = max (f[i - 1][j - 1],f[i - 1][j]) + a[i][j];//加上下方和右下方的最大值
        }
    }

//遍历最底层各位置，找出最大值
    int ans = -INF;
    for (int i = 1;i <= n;i++) 
        ans = max (ans,f[n][i]);
    printf("%d\n",ans);
    return 0;
}
```

```
//思路②：向上爬
#include <iostream>
using namespace std;
const int N = 510;
int n;
int a[N][N];
int f[N][N];
int main () {
//输入数据
    scanf("%d",&n);
    for (int i = 1;i <= n;i++) {
        for (int j = 1;j <= i;j++) 
            scanf("%d",&a[i][j]);
    }

//用三角形最底层数据初始化f最底层数组 -- 分析点②
    for (int i = 1;i <= n;i++) 
        f[n][i] = a[n][i];

//遍历每个位置，记录最大路径
//对比往下走，往上①不必初始化f数组负无穷大 ②不必担心越界访问到非三角形区域
    for (int i = n - 1;i >= 1;i--) {
        for (int j = 1;j <= i;j++) {//第i行共有i个数据
            f[i][j] = max (f[i + 1][j],f[i + 1][j + 1]) + a[i][j];
        }
    }
    
    printf("%d\n",f[1][1]);
    return 0;
}
```

### 例题2:最长上升子序列I

-   题目链接：[895\. 最长上升子序列 - AcWing题库]
    
-   动态规划
    
    -   状态表示`f[i]`\==>(考虑用一维表示就能处理了)
        -   集合:所有以第i个数结尾的上升子序列
        -   属性:Max
    -   状态计算 `f[i]=max(f[j],f[j]+1),j=0,1,2,...,i-1`
        -   有一个边界，若前面没有比i小的，`f[i]`为1（自己为结尾）
    -   时间复杂度:`状态数量×每个状态转移的计算量 = n×n = O(n²)`
-   代码分析:
    
    -   最外层i的for循环先确定每个最长序列的结尾数；内层j的for循环是找①在i前面，②且比i小的数的最长序列长度![![[Pasted image 20230313200523.png]]][fig13]
-   具体代码:
    

```
#include <iostream>
using namespace std;
const int N = 1010;
int n;
int a[N],f[N];

int main () {
//数据输入
    scanf("%d",&n);
    for (int i = 1;i <= n;i++) 
        scanf("%d",&a[i]);
        
    int ans = 0; // 找f[i]中记录的最大值，边算边找
    for (int i = 1;i <= n;i++) 
    {
        f[i] = 1; // f[i]默认设为1，前面找不到小于自己的数时就为1
        for (int j = 1; j < i; j++) 
        {
            if (a[j] < a[i]) 
                f[i] = max (f[i],f[j] + 1); // 前面小于自己的数且在其最大上升子序列基础上加上自己，即+1
        }
        ans = max (ans,f[i]);
    }
    
    printf("%d\n",ans);
    return 0;
}
```

-   动态规划常用输出方案的方式：将转移记录下来。（但是是逆序输出的，若想顺序输出，仅需反一下）

```
#include <iostream>
using namespace std;
const int N = 1010;
int n;
int a[N],f[N],g[N];//g记录各位置对应各自的最长序列中的上一个数位置下标

int main () {
//数据输入
    scanf("%d",&n);
    for (int i = 1;i <= n;i++) scanf("%d",&a[i]);
        
    for (int i = 1;i <= n;i++) 
    {
        f[i] = 1; 
        g[i] = 0; 
        for (int j = 1; j < i; j++) 
        {
            if (a[j] < a[i]) 
            if(f[i] < f[j]+1)
            {
            f[i] = f[j] + 1; 
            g[i] = j;//记录最长序列路径里的上一个位置
            } 
        }
    }

//遍历f数组，找最长序列长度
int k=1;//k记录最长序列最末数的下标
for(int i=1;i<=n;i++)
if(f[k]<f[i]) k=i;
    printf("%d\n",f[k]);

//逆序输出最长序列
for (int i = 0,len=f[k];i < len; i++){
printf("%d ",a[k]);
k=g[k];
}

    return 0;
}
```

##### 例题2优化: 最长上升子序列 II

-   题目链接:[896\. 最长上升子序列 II - AcWing题库]
-   待补充

### 例题3:最长公共子序列

-   题目链接:[897\. 最长公共子序列 - AcWing题库]
-   动态规划
    -   状态表示 `f[i,j]`
        
        -   (对比上题\[\[5.动态规划#例题2 最长上升子序列I\]\], 此题中有两个序列, 故考虑用两维来表示, 经验之谈)
        -   集合: 所有在第一个序列的前i个字母中出现,且在第二个序列的前j个字母中出现的子序列
        -   属性: Max
    -   状态计算：![在这里插入图片描述][fig14]
        
    -   时间复杂度:`状态数量×每个状态转移的计算量 = n×n = O(n²)`
        
-   代码分析:
    -   理解角度①：分成四块（如上状态分析）==> 不是很理解
    -   理解角度②：根据`a[i]和b[j]`是否相等，分成两部分。
        -   思路来源：[AcWing 897. 最长公共子序列 - AcWing]
        -   `f[i][j]` 表示在第一个序列的前i个字母中出现并且在第二个序列的前j个字母中出现的最大值
        -   以第i个和第j个字母（即`a[i]和b[j]`）是否相同来划分
            -   如果相同： `f[i][j] = f[i - 1][j - 1] + 1`
            -   如果不相同： `f[i][j] = max(f[i - 1][j], f[i][j - 1])`
                -   因为如果不相同，那么此时`f[i][j]`的值肯定不会大于`f[i - 1][j]和f[i][j - 1]`中的最大值，则一定会等于`f[i - 1][j]和f[i][j - 1]`的最大值
                -   比如a序列：abcde，b序列：bcdf，因为此时"e"与"f"不等，即`a[5]!=b[4]`，所以此时`dp[5][4]=dp[4][3]`，如果此时再`dp[i][j] = dp[i - 1][j - 1] + 1`就多加了
-   具体代码:

```
//思路①：y总写法
#include <iostream>
using namespace std;
const int N = 1010;

int n , m;
char a[N] , b[N];
int f[N][N];
int main()
{
    scanf("%d%d",&n,&m);//字符串A长n；字符串B长m
    scanf("%s%s",a+1,b+1);//字符串输入

    for(int i = 1 ; i <= n ; i++)
        for(int j = 1 ; j <= m ; j++)
        {
            f[i][j] = max(f[i - 1][j] , f[i][j - 1]);//②和③的情况一定存在，所以可以无条件优先判断
            if(a[i] == b[j]) f[i][j] = max(f[i][j] , f[i - 1][j - 1] + 1);
        }                                                       

    printf("%d\n",f[n][m]);

    return 0;
}
```

```
//思路②：根据a[i]和b[j]是否相等划分（更易理解）
#include <iostream>
using namespace std;
const int N = 1010;
int n, m;
char a[N], b[N];
int f[N][N];
int main() 
{
    cin >> n >> m >> a + 1 >> b + 1;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (a[i] == b[j]) {
                f[i][j] = f[i - 1][j - 1] + 1;
            } else {
                f[i][j] = max(f[i - 1][j], f[i][j - 1]);
            }
        }
    }
    cout << f[n][m] << '\n';
    return 0;
}
```

### 例题4:最短编辑距离

-   待补充

### 例题5:编辑距离

-   [899\. 编辑距离 - AcWing题库]
-   待补充

___

## 四. 区间DP

-   区间DP：定义状态的时候,是定义一个区间
    
    -   若分析题目发现要表示一段区间`[i,j]`的某个量，就可考虑用区间dp;
    -   如果是从`[1,i]`的某个量，那么一般是正常的dp，比如背包问题类型。
-   动态规划
    
    -   状态表示 `f[i,j]` (表示从i到j的一段区间)
        -   集合: 所有将第i堆石子到第j堆石子合并成一堆石子的合并方式
        -   属性: Min
    -   状态计算 `f[i]=max(f[j]+1),j=0,1,2,...,i-1`
        -   i < j时，`f[i][j] = min(f[i][k]+f[k+1][j]+s[j]-s[i-1]) , k∈[i,j-1]`
            -   `f[i][k] + f[k+1][j]`代表的是合成`[i~k]`这一堆石子和合成`[k+1~j]`这一堆石子代价
            -   `s[j]-s[i-1]`代表的合并`[i~k]和[k+1~j]` 这两堆石子的代价
        -   i == j时，`f[i][i] = 0`（合并一堆石子代价为 0）
        -   故返回答案：`f[1][n]`
    -   时间复杂度:`状态数量×每个状态转移的计算量 = n²×n = O(n³)`
-   所有的区间dp问题枚举时，通常习惯:
    
    -   第一维通常是：先从小到大枚举区间的长度，并且一般 len = 1 时用来初始化，枚举从 len = 2 开始；
    -   第二维：枚举区间的起点 i（即左端点），而右端点 j 自动获得`j = i + len - 1`
    -   第三维：而后再枚举决策
-   区间dp模板
    
    -   区间 DP 枚举套路：长度+左端点

```
// 区间长度
for (int len = 1; len <= n; len++) {   
// 枚举起点
    for (int i = 1; i + len - 1 <= n; i++) { 
        int j = i + len - 1;  // 区间终点               
        if (len == 1) {
            dp[i][j] = 初始值
            continue;
        }

// 枚举分割点，构造状态转移方程
        for (int k = i; k < j; k++) {        
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + w[i][j]);
        }
    }
}
```

### 例题:石子合并

-   [282\. 石子合并 - AcWing题库]
    
-   思路：![请添加图片描述][fig15]
    
    -   状态转移方程：`f[l][r] = min(f[l][r], f[l][k] + f[k + 1][r] + s[r] - s[l - 1]);`
        -   `f[l][k] + f[k + 1][r]`：`f[L,k]和f[k+1,R]`两堆各自历史合并的体力；
        -   `s[r] - s[l - 1]`：最后一步`f[L,R]`的代价和==>采用前缀和解决
-   代码分析:
    
    -   由于题目中要求每次只能合并相邻的两堆石子，故不能采取贪心做法（即不能从小到大排序后再两两合并）
    -   分析点①：为什么当len从2开始，就不用memset f数组，也不用边界初始化，只需`f[l][r] = 1e8;` 呢？
-   具体代码:
    

```
#include <iostream>
#include <cstring>

using namespace std;

const int N = 310;

int n;
int a[N], s[N];//a[]读取每个石堆的质量；s[]前缀和
int f[N][N];//状态表示

int main() {
    //输入数据，并且计算从a[1]到a[i]之和的s[]
    scanf("%d",&n);
    for (int i = 1; i <= n; i ++) {
        scanf("%d",&a[i]);
        s[i] += s[i - 1] + a[i];//预处理前缀和
    }

    memset(f, 0x3f, sizeof f);//由于要求的是最小值，故f数组初始化为最大值
    //①先从小到大枚举区间长度
    for (int len = 1; len <= n; len ++) { // len表示[i, j]的元素个数
        //②再枚举区间的左端点
        for (int i = 1; i + len - 1 <= n; i ++) {
            int l =i, r=i + len - 1;// 计算得右端点
//f[l][r]=1e8;//分析点①
            if (len == 1) {//合并自身代价为0
                f[l][r] = 0;  // 边界初始化
                continue;//不用继续了
            }

            //③而后枚举决策
            for (int k = l; k <= r-1; k ++) { // 必须满足k + 1 <= r
                f[l][r] = min(f[l][r], f[l][k] + f[k + 1][r] + s[r] - s[l - 1]);
            }
        }
    }

    printf("%d\n",f[1][n]);
    
    return 0;
}
```

___

## 计数类DP

### 例题:整数划分

-   [900\. 整数划分 - AcWing题库]
-   待补充

___

## 数位统计DP

-   数位dp要点: 分情况讨论
-   求从`[a,b]`中0~9分别出现的次数, 思路如下:
    -   实现count(n,x)函数 ==> 用于求1~n中x出现的次数
    -   则 `count(b,x) - count(a-1,x)` ==> 求`[a,b]`中0~9分别出现的次数

### 例题:计数问题

-   [338\. 计数问题 - AcWing题库]
-   待补充

___

## 状态压缩DP

-   状态压缩：把很多的状态压缩到整数当中，故一般n为20是极限情况了
    -   故当看到n偏小时，就能考虑用状态压缩解决

### 例题1:蒙德里安的梦想(有难度)

-   [291\. 蒙德里安的梦想 - AcWing题库]
-   待补充

### 例题2:最短Hamilton路径

-   [91\. 最短Hamilton路径 - AcWing题库]
-   待补充

___

## 树形DP

-   树形dp只要接受了一开始的陌生思维后，一般这类的题偏简单

### 例题:没有上司的舞会

-   [285\. 没有上司的舞会 - AcWing题库]
-   待补充

___

## 记忆化搜索

-   待补充

___

## 蓝桥杯复习DP相关

### 课堂例题1：01背包问题

-   链接：[2\. 01背包问题 - AcWing题库]
    
-   思路：![请添加图片描述][fig16]
    
-   代码分析：
    
-   具体代码
    

```
#include <iostream>
using namespace std;
const int N = 1010;
int n, m;
int f[N];

int main()
{
    cin >> n >> m;
    for (int i = 0; i < n; i ++ )
    {
        int v, w;
        cin >> v >> w;
        for (int j = m; j >= v; j -- )
            f[j] = max(f[j], f[j - v] + w);
    }

    cout << f[m] << endl;

    return 0;
}
```

### 课堂例题2：摘花生

-   链接：[1015\. 摘花生 - AcWing题库]
    
-   动态规划DP思路分析
    
    -   状态表示`f[i][j]`：题目是两维坐标，并且从时间复杂度可看出不能超过两维（超出两维，时间复杂度就会超出限制）
        -   集合：`f[i][j]`为所有从起点(1, 1)到达(i, j)的合法路线的集合
        -   属性：Max
    -   状态计算：![在这里插入图片描述][fig17]
-   代码分析：
    
-   具体代码
    

```
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
const int N = 110;
int n, m;
int w[N][N];
int f[N][N];

int main()
{
    int T;
    cin >> T;
    while (T -- )
    {
        cin >> n >> m;
        for (int i = 1; i <= n; i ++ )
            for (int j = 1; j <= m; j ++ )
                cin >> w[i][j];

        memset(f, 0, sizeof f);
        for (int i = 1; i <= n; i ++ )
            for (int j = 1; j <= m; j ++ )
                f[i][j] = max(f[i - 1][j], f[i][j - 1]) + w[i][j];

        cout << f[n][m] << endl;
    }

    return 0;
}
```

### 课堂例题3：最长上升子序列

-   链接：[895\. 最长上升子序列 - AcWing题库]
-   动态规划DP思路分析
    -   状态表示`f[i]`：
        -   集合：所有以i结尾的严格单调上升子序列的集合
        -   属性：Max
    -   状态计算：
-   代码分析：
    -   看数据`N∈[1,1000]`，因此时间复杂度要控制在O(N²) ~ O(N²logN)，故可得状态表示应该在一维~两维
-   具体代码

```
#include <iostream>
#include <algorithm>
using namespace std;
const int N = 1010;

int n;
int a[N];
int f[N];

int main()
{
    cin >> n ;
    for (int i = 1; i <= n; i ++ ) cin >> a[i];

    int res = 0;
    for (int i = 1; i <= n; i ++ )
    {
        f[i] = 1;
        for (int j = 1; j < i; j ++ )
            if (a[i] > a[j])
                f[i] = max(f[i], f[j] + 1);

        res = max(res, f[i]);
    }

    cout << res << endl;

    return 0;
}
```

### 课后习题1：地宫取宝

-   链接：[1212\. 地宫取宝 - AcWing题库]
-   代码分析：
-   具体代码

```

```

### 课后习题2：波动数列

-   链接：[1214\. 波动数列 - AcWing题库]
-   代码分析：
-   具体代码

```

```

[fig1]: https://img-blog.csdnimg.cn/e218f544f2a44be49f35faedb04dc0ec.png
[fig2]: https://img-blog.csdnimg.cn/3b80a38ff6cf4d10844b1f2d35963671.png
[fig3]: https://img-blog.csdnimg.cn/0300661783ca4697923f842610172cc6.png
[fig4]: https://img-blog.csdnimg.cn/83075ed21b9c41fa94a8b46621577680.png
[fig5]: https://img-blog.csdnimg.cn/a7b3f4812ec64caabb3f3ad630fdcd65.png
[fig6]: https://img-blog.csdnimg.cn/6dcb59a0fe5b421991519e6deb56ab59.png
[fig7]: https://img-blog.csdnimg.cn/0ca7a08270774e3e95a87893e07f85ed.png
[fig8]: https://img-blog.csdnimg.cn/92c79897a5af45a9b957807fd2836783.png
[fig9]: https://img-blog.csdnimg.cn/f0b44c5d35334b139937349b03a86c4d.png
[fig10]: https://img-blog.csdnimg.cn/0dacee77958e4e99b78e40b5f4f5cd8f.png
[fig11]: https://img-blog.csdnimg.cn/2952aa7d544b4c02ba72853d8458dc1c.png
[fig12]: https://img-blog.csdnimg.cn/b4505acaf6414e07b4e84654f873390a.png
[fig13]: https://img-blog.csdnimg.cn/517163297086481dac307908200ef6f6.png
[fig14]: https://img-blog.csdnimg.cn/c0f462a8f73f4f9493d653b2b4b41c55.png
[fig15]: https://img-blog.csdnimg.cn/8bbf905ddfbc42c3a136474d656a6439.png
[fig16]: https://img-blog.csdnimg.cn/b1550d2d97bf4a2cb961b471bb9bd625.png
[fig17]: https://img-blog.csdnimg.cn/d5f0365aeea4454289631ab42e50385b.png

[背包问题]: https://so.csdn.net/so/search?q=%E8%83%8C%E5%8C%85%E9%97%AE%E9%A2%98&spm=1001.2101.3001.7020
[2\. 01背包问题 - AcWing题库]: https://www.acwing.com/problem/content/2/
[2\. 01背包问题 - AcWing题库]: https://www.acwing.com/problem/content/discussion/content/2807/
[01背包问题]: https://so.csdn.net/so/search?q=01%E8%83%8C%E5%8C%85%E9%97%AE%E9%A2%98&spm=1001.2101.3001.7020
[3\. 完全背包问题 - AcWing题库]: https://www.acwing.com/problem/content/3/
[4\. 多重背包问题 I - AcWing题库]: https://www.acwing.com/problem/content/description/4/
[5\. 多重背包问题 II - AcWing题库]: https://www.acwing.com/problem/content/5/
[AcWing 5. 二进制优化，它为什么正确，为什么合理，凭什么可以这样分？ - AcWing]: https://www.acwing.com/solution/content/20115/
[2\. 01背包问题 - AcWing题库]: https://www.acwing.com/problem/content/2/
[898\. 数字三角形 - AcWing题库]: https://www.acwing.com/problem/content/900/
[895\. 最长上升子序列 - AcWing题库]: https://www.acwing.com/problem/content/897/
[896\. 最长上升子序列 II - AcWing题库]: https://www.acwing.com/problem/content/898/
[897\. 最长公共子序列 - AcWing题库]: https://www.acwing.com/problem/content/899/
[AcWing 897. 最长公共子序列 - AcWing]: https://www.acwing.com/solution/content/8111/
[899\. 编辑距离 - AcWing题库]: https://www.acwing.com/problem/content/901/
[282\. 石子合并 - AcWing题库]: https://www.acwing.com/problem/content/284/
[900\. 整数划分 - AcWing题库]: https://www.acwing.com/problem/content/902/
[338\. 计数问题 - AcWing题库]: https://www.acwing.com/problem/content/340/
[291\. 蒙德里安的梦想 - AcWing题库]: https://www.acwing.com/problem/content/293/
[91\. 最短Hamilton路径 - AcWing题库]: https://www.acwing.com/problem/content/93/
[285\. 没有上司的舞会 - AcWing题库]: https://www.acwing.com/problem/content/287/
[2\. 01背包问题 - AcWing题库]: https://www.acwing.com/problem/content/2/
[1015\. 摘花生 - AcWing题库]: https://www.acwing.com/problem/content/1017/
[895\. 最长上升子序列 - AcWing题库]: https://www.acwing.com/problem/content/897/
[1212\. 地宫取宝 - AcWing题库]: https://www.acwing.com/problem/content/1214/
[1214\. 波动数列 - AcWing题库]: https://www.acwing.com/problem/content/1216/
