Notes Link - 
- [Lecture - OOPS](https://docs.google.com/document/d/1uv9EdLaG9TK7iNcMneLeEaChzvmXU9Xu_Uv5iZwswFk/edit?tab=t.0)

### OOPS

4 pillars: Abstraction, Encapsulation, Inheritance, Polymorphism

1. Polymorphism
   - Function Overloading - same name, different params. Resolved at compile time (static binding)
   - Function Overriding - subclass redefines superclass method. Resolved at runtime (dynamic binding)

2. Inheritance

   Arrow points child ---> parent. Solid = `extends`, dotted = `implements`

   Legend: 🟦 parent &nbsp; 🟩 child &nbsp; 🟧 grandchild &nbsp; 🟪 interface

   - Single Level

     ```mermaid
     graph BT
       Dog --> Animal
       classDef parent fill:#4a90d9,stroke:#1b4d75,stroke-width:2px,color:#fff
       classDef child fill:#57a773,stroke:#255c3a,stroke-width:2px,color:#fff
       class Animal parent
       class Dog child
     ```

   - Multi Level

     ```mermaid
     graph BT
       Puppy --> Dog --> Animal
       classDef parent fill:#4a90d9,stroke:#1b4d75,stroke-width:2px,color:#fff
       classDef child fill:#57a773,stroke:#255c3a,stroke-width:2px,color:#fff
       classDef grand fill:#e08e45,stroke:#8a4c15,stroke-width:2px,color:#fff
       class Animal parent
       class Dog child
       class Puppy grand
     ```

   - Hierarchical

     ```mermaid
     graph BT
       Dog --> Animal
       Cat --> Animal
       classDef parent fill:#4a90d9,stroke:#1b4d75,stroke-width:2px,color:#fff
       classDef child fill:#57a773,stroke:#255c3a,stroke-width:2px,color:#fff
       class Animal parent
       class Dog,Cat child
     ```

   - Hybrid - mix of above, needs an interface in Java

     ```mermaid
     graph BT
       Dog --> Animal
       Cat --> Animal
       Puppy --> Dog
       Puppy -.-> Pet
       classDef parent fill:#4a90d9,stroke:#1b4d75,stroke-width:2px,color:#fff
       classDef child fill:#57a773,stroke:#255c3a,stroke-width:2px,color:#fff
       classDef grand fill:#e08e45,stroke:#8a4c15,stroke-width:2px,color:#fff
       classDef iface fill:#9b6bc4,stroke:#4f2d73,stroke-width:2px,color:#fff
       class Animal parent
       class Dog,Cat child
       class Puppy grand
       class Pet iface
     ```

   - Multiple - NOT allowed for classes in Java (diamond problem), do it with interfaces

     ```mermaid
     graph BT
       Duck -.-> Swimmable
       Duck -.-> Flyable
       classDef child fill:#57a773,stroke:#255c3a,stroke-width:2px,color:#fff
       classDef iface fill:#9b6bc4,stroke:#4f2d73,stroke-width:2px,color:#fff
       class Swimmable,Flyable iface
       class Duck child
     ```

C++ allows Multiple Inheritance of classes directly. Java forbids it, allows many `implements` instead.

3. Abstraction
   - Show what an object does, hide how it does it
   - Done with `abstract` classes and `interface`

4. Encapsulation
   - Bundle data + methods in one class, hide state with `private` fields, expose via getters/setters
   - Packages group related classes (organisation), not encapsulation itself

   - 4 Access Modifiers (least to most permissive)
     - private
       - same class only
     - default (package-private, no keyword written)
       - any class in the same package
     - protected
       - same class + same package + subclass in another package (through inheritance only)
     - public
       - any class anywhere
