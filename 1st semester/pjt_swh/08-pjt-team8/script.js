/**
 * 제공 코드
 */
// 기본 작가, 분류, 도서 데이터 (JavaScript Array)
const categories = categoryRawData
const authors = authorRawData
const books = bookRawData
// 데이터 확인
console.log(categories.length)
console.log(categories[0])
console.log(authors.length)
console.log(authors[0])
console.log(books.length)
console.log(books[0])

// 도서 검색 관련 요소들
const searchInput = document.querySelector('#search-input')
const searchButton = document.querySelector('#search-button')
const resetButton = document.querySelector('#reset-button');
const filterTitleRadio = document.querySelector('#filter-title');
const filterAuthorRadio = document.querySelector('#filter-author');
const filterCategoryRadio = document.querySelector('#filter-category');
let favoriteTitles = []; 

/**
 * 대부분의 작업은 script.js에서 진행해도 무방하나 원한다면 js 파일 추가 가능
 * HTML 요소 추가를 위한 `.innerHTML` 사용 금지, 요소의 내용을 비우는 용도로는 사용 가능 (`.innerHTML = ```)
 */

// 기능 A =======================================================================
const bookListRowTag = document.querySelector('#book-list-row')

function createBookCard(book) {
  const colDiv = document.createElement('div');
  colDiv.classList.add('col-12', 'col-sm-6', 'col-md-4', 'col-lg-3', 'mb-4');

  const cardDiv = document.createElement('div');
  cardDiv.classList.add('card', 'h-100');
  cardDiv.style.height = '200px';


  const cardImage = document.createElement('img');
  cardImage.classList.add('card-img-top', 'object-fit-contain')
  cardImage.alt = book.title || 'Book cover image';
  // cardImage.style.height = '150px';

  const imageUrl = book.cover ? book.cover : 'stack-of-books.png';
  cardImage.src = imageUrl;

  const cardBodyDiv = document.createElement('div');
  cardBodyDiv.classList.add('card-body');

  const h5Tag = document.createElement('h5')
  h5Tag.classList.add('card-title')
  h5Tag.textContent = book.title.length > 30 ? book.title.substring(0, 30) + '...' : book.title;


  cardBodyDiv.appendChild(h5Tag);
  cardDiv.appendChild(cardImage);
  cardDiv.appendChild(cardBodyDiv);
  colDiv.appendChild(cardDiv);

  // 기능 E
 const cardA = document.createElement('a')
  cardA.href = '#' 
  
  // 1. 현재 이 책 제목이 즐겨찾기 목록에 있는지 확인
  // (book.id -> book.title로 변경)
  const isFav = favoriteTitles.includes(book.title);

  // 2. 상태에 따라 버튼 색상 및 텍스트 설정
  if (isFav) {
      cardA.classList.add("btn", "btn-danger", "w-100");
      cardA.textContent = '즐겨찾기 취소';
  } else {
      cardA.classList.add("btn", "btn-primary", "w-100");
      cardA.textContent = '즐겨찾기';
  }

  // 3. 클릭 이벤트 추가
  
  cardA.addEventListener('click', (e) => {
      e.preventDefault();

      // (book.id -> book.title로 변경)
      if (favoriteTitles.includes(book.title)) {
          // 이미 있으면 삭제
          favoriteTitles = favoriteTitles.filter(title => title !== book.title);
          cardA.classList.replace("btn-danger", "btn-primary");
          cardA.textContent = '즐겨찾기';
      } else {
          // 없으면 추가
          favoriteTitles.push(book.title);
          cardA.classList.replace("btn-primary", "btn-danger");
          cardA.textContent = '즐겨찾기 취소';
      }

      // 현재 'Favorites' 탭을 보고 있다면 화면 즉시 갱신
      const favoritesContainer = document.querySelector('#favorites-container');
      if (!favoritesContainer.classList.contains('d-none')) {
          renderFavorites(); 
          
          // 목록이 비워지면 홈으로 이동
          if (favoriteTitles.length === 0) {
              alert('즐겨찾기된 도서가 없어 홈으로 이동합니다.');
              document.querySelector('#home-nav').click();
          }
      }


  });
  // -------------------------------------------------------

  cardBodyDiv.appendChild(cardA);

  return colDiv;
}

function renderBookList(bookList) {
  bookListRowTag.innerHTML = '';
  const listToRender = bookList || books;
  listToRender.forEach(book => {
    const bookCard = createBookCard(book);
    bookListRowTag.appendChild(bookCard);
  });
}

document.addEventListener('DOMContentLoaded', () => {
  renderBookList();
});
// 기능 A 끝 ====================================================================

// -------------------------------------------------------
// [추가 3] 탭 전환 및 즐겨찾기 목록 렌더링 로직 (파일 맨 아래에 추가)
// -------------------------------------------------------
const homeNav = document.querySelector('#home-nav');
const createNav = document.querySelector('#create-nav');
const favoritesNav = document.querySelector('#favorites-nav');

// 기능 B =======================================================================
const getAuthorNameById = (id) => authors.find(a => a.id === id)?.name || '';
const getCategoryNameById = (id) => categories.find(c => c.id === id)?.name || '';

function performSearch(searchTerm) {
  if (!searchTerm || searchTerm.trim() === '') {
    alert('검색어를 입력하세요.');
    return;
  }
  // 대소문자 구분 안함(일괄적으로 소문자로 변경하여 search)
  const trimmedTerm = searchTerm.trim().toLowerCase();

  let searchKey = '';
  if (filterTitleRadio.checked) {
    searchKey = 'title';
  } else if (filterAuthorRadio.checked) {
    searchKey = 'author';
  } else if (filterCategoryRadio.checked) {
    searchKey = 'category';
  }

  const filteredBooks = books.filter(book => {
    let targetValue = '';


    if (searchKey === 'title') {
      targetValue = book.title || '';
    } else if (searchKey === 'author') {
      targetValue = getAuthorNameById(book.authorId);
    } else if (searchKey === 'category') {
      targetValue = getCategoryNameById(book.categoryId);
    }

    return targetValue.toLowerCase().includes(trimmedTerm)
  });

  renderBookList(filteredBooks);
}
function resetSearch() {
  searchInput.value = '';
  filterTitleRadio.checked = true;
  renderBookList(books);
}

searchButton.addEventListener('click', () => {
  performSearch(searchInput.value);
});

searchInput.addEventListener('keypress', (event) => {
  if (event.key === 'Enter') {
    performSearch(searchInput.value);
  }
})

resetButton.addEventListener('click', resetSearch)



// 기능 B 끝 =====================================================================

// 기능 C =======================================================================
// 1. 필요한 요소들을 선택합니다.
const homeContainer = document.querySelector('#home-container');
const createContainer = document.querySelector('#create-container');

const homeNavBtn = document.querySelector('#home-nav');
const createNavBtn = document.querySelector('#create-nav');

// 1. Create 버튼 클릭 시
createNavBtn.addEventListener('click', function () {
  // Home 화면 숨기기 (homeContainer 사용)
  homeContainer.classList.add('d-none');
  // Create 화면 보이기
  createContainer.classList.remove('d-none');

  // (선택사항) 버튼 활성화 스타일
  createNavBtn.classList.add('active');
  homeNavBtn.classList.remove('active');
});

// 2. Home 버튼 클릭 시
homeNavBtn.addEventListener('click', function () {
  // Home 화면 보이기 (homeContainer 사용)
  homeContainer.classList.remove('d-none');
  // Create 화면 숨기기
  createContainer.classList.add('d-none');
  favoritesContainer.classList.add('d-none');

  // (선택사항) 버튼 활성화 스타일
  homeNavBtn.classList.add('active');
  createNavBtn.classList.remove('active');

  renderBookList();
});

// 기능 C 끝 =======================================================================

// 기능 D =======================================================================
// 1. 필요한 DOM 요소 선택
const createForm = document.querySelector('#create-form');
const errorList = document.querySelector('#create-book-errors');
function findOrCreateAutorId(list, name) {
  let item = list.find(i => i.name === name);

  if (item) {
    return item.id;
  } else {
    const newId = list.lenght > 0 ? Math.max(list.map(i => i.id)) + 1 : 1;
    list.push({ id: newId, author: name});
    return newId;
  }
}

function findOrCreateCategoryId(list, name) {
  let item = list.find(i => i.name === name);
  if (item) {
    return item.id;
  } else {
    const newId = list.lenght > 0 ? Math.max(list.map(i => i.id)) + 1 : 1;
    list.push({ id: newId, category: name});
    return newId;
  }
}

// 2. 폼 제출(Submit) 이벤트 리스너 (버튼 클릭 & 엔터키 모두 동작함)
createForm.addEventListener('submit', function (event) {
  // (1) 브라우저의 기본 새로고침 동작 중단
  event.preventDefault();

  // (2) 에러 메시지 초기화 (이전 에러 지우기)
  errorList.innerHTML = '';
  let hasError = false;

  // (3) 입력값 가져오기 (양쪽 공백 제거)
  const title = document.querySelector('#title-input').value.trim();
  const author = document.querySelector('#author-input').value.trim();
  const desc = document.querySelector('#desc-input').value.trim();
  const category = document.querySelector('#category-input').value.trim();
  let imgUrl = document.querySelector('#img-input').value.trim();

  // (4) 유효성 검사: 필수 입력값 확인
  if (!title) {
    addErrorMessage('제목을 입력해주세요.');
    hasError = true;
  }
  if (!author) {
    addErrorMessage('작가를 입력해주세요.');
    hasError = true;
  }
  if (!desc) {
    addErrorMessage('소개를 입력해주세요.');
    hasError = true;
  }
  if (!category) {
    addErrorMessage('분류를 입력해주세요.');
    hasError = true;
  }

  // 에러가 하나라도 있으면 함수 종료 (데이터 추가 안 함)
  if (hasError) {
    return;
  }

  // (5) 이미지 URL 검증 로직
  // http로 시작하지 않으면 빈 문자열로 대체
  if (!imgUrl.startsWith('http')) {
    imgUrl = '';
  }

  // (6) 새로운 도서 객체 생성
  const finalAuthorId = findOrCreateAutorId(authors, author);
  const finalcategoryId = findOrCreateCategoryId(categories, category);

  const newBook = {
    title: title,
    description: desc,
    authorId: finalAuthorId,
    cover: imgUrl, // 검증된 URL 또는 빈 값
    categoryId: finalcategoryId
  };

  // (7) 데이터 배열 업데이트
  // books는 전역 변수로 선언된 도서 목록 배열이라고 가정합니다.
  books.unshift(newBook); // 배열의 '가장 앞'에 추가

  // (선택사항) 작가, 카테고리 배열 업데이트 (중복 체크 후 추가)
  if (!authors.includes(author)) authors.push(author);
  if (!categories.includes(category)) categories.push(category);


  createForm.reset();


  // 페이지 처음 로드될 때 한번 실행 (초기 데이터 표시)
  renderBookList(books);


  // 3. '도서 목록' 탭으로 화면 전환 (아까 구현한 변수 사용)
  document.querySelector('#create-container').classList.add('d-none');
  document.querySelector('#home-container').classList.remove('d-none');

  // 4. 네비게이션 버튼 스타일 업데이트 (선택사항)
  document.querySelector('#create-nav').classList.remove('active');
  document.querySelector('#home-nav').classList.add('active');

  alert('도서가 추가되었습니다!');
});


// 헬퍼 함수: 에러 메시지를 li 태그로 만들어 추가
function addErrorMessage(msg) {
  const li = document.createElement('li');
  li.textContent = msg;
  li.style.color = 'red'; // 간단한 스타일링 (CSS로 빼도 됨)
  errorList.appendChild(li);
}


// 기능 D 끝 =======================================================================

// 기능 E =======================================================================



const favoritesContainer = document.querySelector('#favorites-container'); 
const favoritesListRow = document.querySelector('#favorites-list-row'); 

// 3. Favorites 탭 클릭
favoritesNav.addEventListener('click', () => {
    homeContainer.classList.add('d-none');
    createContainer.classList.add('d-none');
    favoritesContainer.classList.remove('d-none');
    renderFavorites(); 
});

// 4. 즐겨찾기 목록 그리는 함수
function renderFavorites() {
    favoritesListRow.innerHTML = ''; 

    // (book.id -> book.title로 변경하여 필터링)
    const favBooks = books.filter(book => favoriteTitles.includes(book.title));

    if (favBooks.length === 0) {
        favoritesListRow.innerHTML = '<div class="text-center mt-5 fs-4 text-secondary">즐겨찾기한 도서가 없습니다.</div>';
    } else {
        favBooks.forEach(book => {
            const card = createBookCard(book); 
            favoritesListRow.appendChild(card);
        });
    }
}

// 기능 E 끝 =======================================================================
