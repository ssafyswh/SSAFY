// store/articles.js

import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'

export const useArticleStore = defineStore('article', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const articles = ref([
    // { id: 1, title: 'Article 1', content: 'content of Article1'},
    // { id: 2, title: 'Article 2', content: 'content of Article2'},
  ])

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`
    })
      .then(res => {
        console.log(res.data)
        articles.value = res.data
      })
      .catch(err => console.log(err))
  }

  return { articles, getArticles, API_URL }
}, { persist: true })
