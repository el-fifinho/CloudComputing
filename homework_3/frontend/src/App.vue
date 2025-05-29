<!-- frontend/src/App.vue -->
<template>
  <div class="min-h-screen bg-gray-100 flex flex-col items-center p-4">
    <h1 class="text-3xl font-bold mb-6">YouTube Transcriber & Translator</h1>

    <div class="bg-white shadow-xl rounded-2xl p-6 w-full max-w-xl">
      <label class="block mb-2 font-semibold">YouTube URL:</label>
      <input v-model="youtubeUrl" class="w-full p-2 border rounded mb-4" placeholder="Enter YouTube video URL" />

      <label class="block mb-2 font-semibold">Target Language (e.g., 'es', 'fr', 'ro'):</label>
      <input v-model="targetLang" class="w-full p-2 border rounded mb-4" placeholder="Enter target language code" />

      <button @click="submit" :disabled="loading" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
        {{ loading ? 'Processing...' : 'Submit' }}
      </button>
    </div>

    <div v-if="result" class="mt-6 bg-white shadow-xl rounded-2xl p-6 w-full max-w-xl">
      <h2 class="text-xl font-semibold mb-2">Transcript:</h2>
      <p class="mb-4 whitespace-pre-wrap">{{ result.transcript }}</p>

      <h2 class="text-xl font-semibold mb-2">Translated:</h2>
      <p class="whitespace-pre-wrap">{{ result.translated }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      youtubeUrl: '',
      targetLang: '',
      loading: false,
      result: null
    };
  },
  methods: {
    async submit() {
      if (!this.youtubeUrl || !this.targetLang) return;
      this.loading = true;
      this.result = null;
      try {
        const response = await axios.post('/api/process', {
          url: this.youtubeUrl,
          lang: this.targetLang
        });
        this.result = response.data;
      } catch (error) {
        alert('Error: ' + (error.response?.data?.error || error.message));
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>

<style>
body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
</style>
