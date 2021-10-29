// function to get the id of the blog to be deletd and adding it as an input tag to the form

function deleteBlog(blogid){
    input = document.createElement("input");
    input.type = "hidden";
    input.className = "d-none";
    input.value = blogid;
    input.name = "blogtodelete";
    document.getElementById("blogtodelete").appendChild(input);
}

function editBlog(blogid){
    document.body.scrollTop = document.documentElement.scrollTop = 0;
    title = document.getElementById("blog"+blogid+"title").innerHTML;
    body = document.getElementById("blog"+blogid+"body").innerHTML;
    document.getElementById("newBlog").classList.add("show");
    document.getElementById("title").value = title;
    document.getElementById("blogbody").innerHTML = body;
    input = document.createElement("input");
    input.type="hidden";
    input.value = blogid;
    input.id = "blogtoedit";
    input.name = "blogtoedit";
    document.getElementById("addBlog").appendChild(input);
}

function resetBody(){
    let input = document.getElementById("blogtoedit");
    if (input){
        input.parentNode.removeChild(input);
    }
    document.getElementById("title").value = "";
    document.getElementById("blogbody").innerHTML = "";
}
