const natalia = {
  name: "Natalia",
  age: 20,
  cursosAprobados: [
    "Curso Definitivo de HTML y CSS",
    "Curso Práctico de HTML y CSS",
  ],
  aprobarCurso(nuevoCursito) {
    this.cursosAprobados.push(nuevoCursito);
  },
};


function Student(name, age, cursosAprobados) {
  this.name = name;
  this.age = age;
  this.cursosAprobados = cursosAprobados;
  // this.aprobarCurso = function (nuevoCursito) {
  //   this.cursosAprobados.push(nuevoCursito);
  // }
}

Student.prototype.aprobarCurso = function (nuevoCursito) {
  this.cursosAprobados.push(nuevoCursito);
}

const juanita = new Student(
  "Juanita Alejandra",
  15,
  [
    "Curso de Introducción a la Producción de Videojuegos",
    "Curso de Creación de Personajes",
  ],
);

// Prototipos con la sintaxis de clases
class Student2 {
  constructor({ 
    name, 
    cursosAprobados = [], 
    age, 
    email,
    facebook,
    twitter,
    spotify
  }) { 
    this.name = name;
    this.email = email; 
    this.age = age; 
    this.cursosAprobados = cursosAprobados;
    this.facebook = facebook;
    this.twitter = twitter;
    this.spotify =  spotify
  }
  aprobarCurso(nuevoCursito) { 
    this.cursosAprobados.push(nuevoCursito)}
}

const miguelito = new Student2({
  name: "Miguel",
  age: 28,
  cursosAprobados: [
    "Curso de Analisis",
    "Curso de principios"
  ],
  email: "miguelito@platzi.com",
});



// Ventajas de la programación orientada a objetos

class Course {
  constructor({
    id,
    name,
    teacher,
    lessons = [],
  }) {
    this.id = id;
    this.name = name;
    this.teacher = teacher;
    this.lessons = lessons;
  }
}

class LearningPath {
  constructor({
    id,
    name,
    courses = [],
  }) {
    this.id = id;
    this.name = name;
    this.courses = courses;
  }

  addCourse(course) {
    this.courses.push(course);
  }

  replaceCourse(oldCourse, newCourse) {
    const oldCourseIndex = this.courses.findIndex(course => course.id === oldCourse.id);

    if (oldCourseIndex !== -1) {
      this.courses[oldCourseIndex] = newCourse;
    }

    return this.courses;
  }

  deleteCourse(oldCourse) {
    const courseIndex = this.courses.findIndex(course => course.id === oldCourse.id);
    this.courses.splice(courseIndex, 1);

    return this.courses;
  }
}

/* 
const reactNativeLearningPath = new LearningPath({
  id: 'react-native',
  name: 'Desarrollo de Apps con React Native',
  courses: [
    new Course({ 
      id: 'basico-javascript', 
      name: 'Curso Básico de JavaScript', 
      teacher: 'Diego De Granda',
    }),
    new Course({
      id: 'ecmascript-6',
      name: 'Curso de ECMAScript 6+',
      teacher: 'Orlando Naipes',
    }),
    // etc...
  ]
})
*/


const escuelaWeb = new LearningPath();
const escuelaData = new LearningPath();
const escuelaVgs = new LearningPath();

class Student {
  constructor({
    name,
    email,
    username,
    twitter = undefined,
    instagram = undefined,
    facebook = undefined,
    approvedCourses = [],
    learningPaths = [],
  }) {
    this.name = name;
    this.email = email;
    this.username = username;
    this.socialMedia = {
      twitter,
      instagram,
      facebook,
    };
    this.approvedCourses = approvedCourses;
    this.learningPaths = learningPaths;
  }
}

const juan2 = new Student({
  name: "JuanDC",
  username: "juandc",
  email: "juanito@juanito.com",
  twitter: "fjuandc",
  learningPaths: [
    escuelaWeb,
    escuelaVgs,
  ],
});

const miguelito2 = new Student({
  name: "Miguelito",
  username: "migelitofeliz",
  email: "miguelito@juanito.com",
  instagram: "migelito_feliz",
  learningPaths: [
    escuelaWeb,
    escuelaData,
  ],
});

