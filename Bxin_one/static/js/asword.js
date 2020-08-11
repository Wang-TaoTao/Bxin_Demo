// 联想词接口
const url = '/index/assword'
const inputText = document.querySelector('.input_text')
const searchBottom = document.querySelector('.search-bottom')
let ul = ''
let setTime = window.setTimeout(() => {},0)
let movieData = []
function wordDream (movieData) {
    ul = document.createElement('ul')
    ul.className = 'ul_movie'
    movieData.slice(0,10).forEach(item => {
        let li = document.createElement('li')
        li.innerHTML = item.name+' ( '+item.nickname+', '+item.phone +' )'
        ul.appendChild(li)
    })
    searchBottom.appendChild(ul)
}

inputText.addEventListener('input',function () {
    if(!this.value.trim()) {
        searchBottom.style.display = 'none'
        this.onblur()
        return false
    }
    window.clearTimeout(setTime)
    setTime = window.setTimeout(() => {
        $.ajax({
            url,
            method: 'get',
            data:{search:this.value},
            success: function (data) {
                if(!this.value.trim()) {
                    return false
                }
                if(ul) {
                    searchBottom.removeChild(ul)
                }
                searchBottom.style.display = this.value ? 'block' : this.onblur()
                movieData = data.data
                console.log(movieData)
                wordDream.call(this,movieData)
            }.bind(this)
        })
    },500)
})

inputText.addEventListener('focus',function () {
    if(inputText.value) {
        searchBottom.style.display = 'block'
    }
})

inputText.onblur = function () {
    searchBottom.style.display = 'none'
}