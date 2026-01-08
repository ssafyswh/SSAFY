import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  // let id = 0

  const todos = ref([])

  const addTodo = function (todoText) {
    todos.value.push({
      id: Date.now(),
      text: todoText,
      isDone: false
    })
  }

  const deleteTodo = function (selectedId) {
    // 1. findIndex + splice (하나만 삭제)
    const index = todos.value.findIndex((todo) => todo.id === selectedId)
    todos.value.splice(index, 1)

    // 2. filter (전체 배열 재생성)
    // todos.value = todos.value.filter(todo => todo.id !== selectedId)
  }

  const updateTodo = function (selectedId) {
    // 1. forEach (하나만 수정)
    todos.value.forEach((todo) => {
      if (todo.id === selectedId) {
        todo.isDone = !todo.isDone
      }
    })

    // 2. map (전체 배열 재생성)
    // todos.value = todos.value.map((todo) => {
    //   if (todo.id === selectedId) {
    //     todo.isDone = !todo.isDone
    //   }
    //   return todo
    // })
  }

  const doneTodosCount = computed(() => {
    const doneTodos = todos.value.filter((todo) => todo.isDone)
    return doneTodos.length
  })

  return { todos, addTodo, deleteTodo, updateTodo, doneTodosCount }
}, { persist: true })
