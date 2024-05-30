CREATE (:User{name: "Valentina Arenas Lozano", username: "cogdiver"});
CREATE (v:User{name: "Valentina Arenas", username: "cogdiver"});

MATCH (n:User) RETURN n;
MATCH (n) RETURN n;