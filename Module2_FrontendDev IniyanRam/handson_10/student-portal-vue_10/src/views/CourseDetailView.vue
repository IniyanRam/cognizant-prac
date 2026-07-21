<template>
  <div class="details">
    <h2>Course Details</h2>

    <div v-if="course">
      <h3>{{ course.name }}</h3>
      <p><strong>Code:</strong> {{ course.code }}</p>
      <p><strong>Credits:</strong> {{ course.credits }}</p>
      <p><strong>Grade:</strong> {{ course.grade }}</p>

      <button @click="enrollCourse">Enroll</button>
    </div>

    <div v-else>
      <p>Course not found.</p>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

const courses = [
  {
    id: 1,
    name: 'Web Development',
    code: 'CS101',
    credits: 4,
    grade: 'A',
  },
  {
    id: 2,
    name: 'Database Systems',
    code: 'CS102',
    credits: 3,
    grade: 'A+',
  },
  {
    id: 3,
    name: 'Operating Systems',
    code: 'CS103',
    credits: 4,
    grade: 'B+',
  },
  {
    id: 4,
    name: 'Computer Networks',
    code: 'CS104',
    credits: 3,
    grade: 'A',
  },
  {
    id: 5,
    name: 'Machine Learning',
    code: 'CS105',
    credits: 4,
    grade: 'O',
  },
]

const course = computed(() =>
  courses.find((c) => c.id === Number(route.params.id))
)

function enrollCourse() {
  router.push('/profile')
}
</script>

<style scoped>
.details {
  padding: 20px;
}

button {
  margin-top: 15px;
  padding: 10px 18px;
  cursor: pointer;
}
</style>