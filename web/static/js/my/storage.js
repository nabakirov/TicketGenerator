
function getFromStorage(name){
    token = null
    try{
        token = localStorage.getItem(name);
    }
    catch(e){
        token = null;
    }
    return token;
};
function setToStorage(key, name){
    ok = false;
    try{
        localStorage.setItem(key, name);
        ok = true;
    }
    catch(e){
        ok = false;
    }
    return ok;
};
function delFromStorage(key){
    ok = false;
    try{
        localStorage.removeItem(key);
        ok = true;
    }
    catch(e){
        ok = false;
    }
    return ok;
};