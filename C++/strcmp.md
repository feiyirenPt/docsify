---
title: strcmp函数的注意点和易错点
date: 2023-03-28 15:39  
tags: [strcmp,C++]  
source: https://blog.csdn.net/m0_64075307/article/details/123941441  
---
1. strcmp函数比较的不是字符串的长度，而是比较字符串中对应位置上的字符的大小（即比较的是ASCII码值，而且还要注意区分大小写），

如果相同，就比较下一对字符，直到这一对的字符不同或者都遇到`\0`

2. 字符串大小的比较是以ASCII码表上的顺序来决定，此顺序亦为字符的值

3. **比较过程：**

strcmp函数首先将 字符串S1 的第一个字符值减去 字符串S2的第一个字符的值，

若差值为0则再继续比较下一对字符，若差值不为0，则将差值返回

4. **strcmp ( ) 函数的返回值**：

- 若其参数 S1 和 S2 字符串相同则返回0
- 若S1 大于 S2 则返回大于0 的值
- 若S1 小于 S2 则返回小于0 的值

5. **strcmp （ ）函数的模拟实现**：

```cpp
#include <stdio.h>
int my_strcmp(char*, char*);
int main(){
	char arr1[] = "abcdef";
	char arr2[] = "abc";
	printf("%d ", my_strcmp(arr1, arr2));
	return 0;
}
 
int my_strcmp(char*compare1, char*compare2){
	while (*compare1 == *compare2){
		if (*compare1 == '\0'){
			return 0;   //这是俩个字符串相等的情况
		}
		compare1++;
		compare2++;
	}
	if (*compare1 > *compare2){
		return 1;
	}else if (*compare1 < *compare2){
		return -1;
	}
}
```

?> 注意字符串结尾需要自己保证`\0`