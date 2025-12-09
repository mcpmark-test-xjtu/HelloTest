// 文件: src/example.js

function greetUser() {
  // ✅ 修复 1 & 2: 改为单引号，并添加分号
  console.log('Hello World');

  // ✅ 修复 3 & 4: 移除未使用的变量，或者像下面这样使用它们
  const usedVariable = 'This variable is now used';
  console.log(usedVariable);

  // 确保没有未使用的变量残留
}

// ✅ 修复 5: 添加分号
greetUser();