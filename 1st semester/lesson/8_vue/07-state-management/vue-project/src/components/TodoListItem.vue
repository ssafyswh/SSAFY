<template>
  <div>
    <input type="checkbox" name="todo-text" v-model="isDone">
    <label for="todo-text" :class="{ 'is-done': todo.isDone }">{{ todo.text }}</label>
    <button @click="deleteTodo(todo.id)">삭제</button>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { ref, watch } from 'vue'

// 체크박스로 하려면
// 1. 체크박스 클릭
// 2. isDone ref 변경
// 3. watch 감지
// 4. store의 updateTodo 호출
const props = defineProps({
  todo: Object
})

const store = useCounterStore()
const isDone = ref(props.todo.isDone)

watch(isDone, () => {
  store.updateTodo(props.todo.id)
})

const deleteTodo = function (selectedId) {
  store.deleteTodo(selectedId)
}
</script>

<style scoped>
.is-done {
  text-decoration: line-through;
}
</style>
