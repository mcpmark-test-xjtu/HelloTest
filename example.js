// 文件: src/example.js

function greetUser() {
  // ❌ 错误 1: 使用了双引号 ('quotes' 规则冲突)
  // ❌ 错误 2: 缺少分号 ('semi' 规则冲突)
  console.log("Hello World")

  // ❌ 错误 3: 'unusedVariable' 未被使用 ('no-unused-vars' 规则冲突)
  const unusedVariable = "This is a linting error"

  // ❌ 错误 4: 'a' 未被使用 ('no-unused-vars' 规则冲突)
  let a = 1
}

// ❌ 错误 5: 缺少分号 ('semi' 规则冲突)
greetUser()