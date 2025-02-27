package java.patrones;

import java.util.ArrayList;
import java.util.List;

abstract class Observador {
    public abstract void actualizar(CanalDeNoticias sujeto);
}

class CanalDeNoticias {
    private String nombre;
    private String nuevasNoticias;
    private List<Observador> suscriptores;

    public CanalDeNoticias(String nombre) {
        this.nombre = nombre;
        this.nuevasNoticias = "";
        this.suscriptores = new ArrayList<>();
    }

    public void agregarSuscriptor(Observador suscriptor) {
        suscriptores.add(suscriptor);
    }

    public void eliminarSuscriptor(Observador suscriptor) {
        suscriptores.remove(suscriptor);
    }

    public void notificarSuscriptores() {
        for (Observador suscriptor : suscriptores) {
            suscriptor.actualizar(this);
        }
    }

    public void establecerNoticias(String noticias) {
        this.nuevasNoticias = noticias;
        notificarSuscriptores();
        System.out.println("Actualización de noticias en " + this.nombre + ": " + this.nuevasNoticias);
    }

    public String getNombre() {
        return nombre;
    }

    public String getNuevasNoticias() {
        return nuevasNoticias;
    }
}

class Suscriptor extends Observador {
    private String nombre;

    public Suscriptor(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public void actualizar(CanalDeNoticias sujeto) {
        System.out.println("El suscriptor " + this.nombre + " recibió noticias de " + sujeto.getNombre());
        System.out.println("Noticias: " + sujeto.getNuevasNoticias());
    }
}

public class Observe {
    public static void main(String[] args) {
        CanalDeNoticias cnn = new CanalDeNoticias("CNN");
        CanalDeNoticias bbc = new CanalDeNoticias("BBC");

        Suscriptor suscriptor1 = new Suscriptor("Alice");
        Suscriptor suscriptor2 = new Suscriptor("Bob");

        cnn.agregarSuscriptor(suscriptor1);
        bbc.agregarSuscriptor(suscriptor2);

        cnn.establecerNoticias("Última hora: Nuevo descubrimiento en el espacio.");
        bbc.establecerNoticias("Últimas noticias: Crisis política en el país.");
    }
}
