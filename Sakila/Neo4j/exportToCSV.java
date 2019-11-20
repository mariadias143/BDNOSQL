import java.io.FileWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class exportToCSV {
    public static void main(String[] args){

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
        } catch (Exception e){
            e.printStackTrace();
        }

        try {
            String url = "jdbc:mysql://127.0.0.1:3306/sakila?useUnicode=true&characterEncoding=UTF-8&zeroDateTimeBehavior=convertToNull&serverTimezone=GMT";
            String username = "root";
            String password = args[0];
            Connection con = DriverManager.getConnection(url,username,password);

            //Tabela Actor
            String filename = "TabelasCSV/actor.csv";
            FileWriter f = new FileWriter(filename);
            String query = "select * from actor";
            Statement st = con.createStatement();
            ResultSet rs = st.executeQuery(query);
            f.append("actor_id,first_name,last_name,last_update");
            f.append('\n');

            while(rs.next()){
                f.append(String.valueOf(rs.getInt(1)));
                f.append(',');
                f.append(rs.getString(2));
                f.append(',');
                f.append(rs.getString(3));
                f.append(',');
                f.append(String.valueOf(rs.getTimestamp(4)));
                f.append('\n');
            }
            f.flush();
            f.close();

            //Tabela address
            filename = "TabelasCSV/address.csv";
            f = new FileWriter(filename);
            query = "select * from address";
            st = con.createStatement();
            rs = st.executeQuery(query);
            f.append("address_id,address,address2,district,city_id,postal_code,phone,location,last_update");
            f.append('\n');

            while(rs.next()){
                f.append(String.valueOf(rs.getInt(1)));
                f.append(',');
                f.append(rs.getString(2));
                f.append(',');
                f.append(rs.getString(3));
                f.append(',');
                f.append(rs.getString(4));
                f.append(',');
                f.append(String.valueOf(rs.getInt(5)));
                f.append(',');
                f.append(rs.getString(6));
                f.append(',');
                f.append(rs.getString(7));
                f.append(',');
                f.append(String.valueOf(rs.getBytes(8))); // bytes ou blob???
                f.append(',');
                f.append(String.valueOf(rs.getTimestamp(9)));
                f.append('\n');
            }
            f.flush();
            f.close();

            //Tabela category
            filename = "TabelasCSV/category.csv";
            f = new FileWriter(filename);
            query = "select * from category";
            st = con.createStatement();
            rs = st.executeQuery(query);
            f.append("category_id,name,last_update");
            f.append('\n');

            while(rs.next()){
                f.append(String.valueOf(rs.getInt(1)));
                f.append(',');
                f.append(rs.getString(2));
                f.append(',');
                f.append(String.valueOf(rs.getTimestamp(3)));
                f.append('\n');
            }
            f.flush();
            f.close();

            //Tabela city
            filename = "TabelasCSV/city.csv";
            f = new FileWriter(filename);
            query = "select * from city";
            st = con.createStatement();
            rs = st.executeQuery(query);
            f.append("city_id,city,country_id,last_update");
            f.append('\n');

            while(rs.next()){
                f.append(String.valueOf(rs.getInt(1)));
                f.append(',');
                f.append(rs.getString(2));
                f.append(',');
                f.append(String.valueOf(rs.getInt(3)));
                f.append(',');
                f.append(String.valueOf(rs.getTimestamp(4)));
                f.append('\n');
            }
            f.flush();
            f.close();

            //Tabela country
            filename = "TabelasCSV/country.csv";
            f = new FileWriter(filename);
            query = "select * from country";
            st = con.createStatement();
            rs = st.executeQuery(query);
            f.append("country_id,country,last_update");
            f.append('\n');

            while(rs.next()){
                f.append(String.valueOf(rs.getInt(1)));
                f.append(',');
                f.append(rs.getString(2));
                f.append(',');
                f.append(String.valueOf(rs.getTimestamp(3)));
                f.append('\n');
            }
            f.flush();
            f.close();

            //Tabela customer
            filename = "TabelasCSV/customer.csv";
            f = new FileWriter(filename);
            query = "select * from customer";
            st = con.createStatement();
            rs = st.executeQuery(query);
            f.append("customer_id,store_id,first_name,last_name,email,address_id,active,create_date,last_update");
            f.append('\n');

            while(rs.next()){
                f.append(String.valueOf(rs.getInt(1)));
                f.append(',');
                f.append(String.valueOf(rs.getInt(2)));
                f.append(',');
                f.append(rs.getString(3));
                f.append(',');
                f.append(rs.getString(4));
                f.append(',');
                f.append(rs.getString(5));
                f.append(',');
                f.append(String.valueOf(rs.getInt(6)));
                f.append(',');
                f.append(String.valueOf(rs.getBoolean(7)));
                f.append(',');
                f.append(String.valueOf(rs.getDate(8)));
                f.append(' ' + String.valueOf(rs.getTime(8)));
                f.append(',');
                f.append(String.valueOf(rs.getTimestamp(9)));
                f.append('\n');
            }
            f.flush();
            f.close();

            //Tabela film
            filename = "TabelasCSV/film.csv";
            f = new FileWriter(filename);
            query = "select * from film";
            st = con.createStatement();
            rs = st.executeQuery(query);
            f.append("film_id,title,description,release_year,language_id,original_language_id,rental_duration,rental_rate,length,replacement_cost,rating,special_features,last_update");
            f.append('\n');

            while(rs.next()){
                f.append(String.valueOf(rs.getInt(1)));
                f.append(',');
                f.append(rs.getString(2));
                f.append(',');
                f.append(rs.getString(3));
                f.append(',');
                f.append(String.valueOf(rs.getInt(4)));
                f.append(',');
                f.append(String.valueOf(rs.getInt(5)));
                f.append(',');
                f.append(String.valueOf(rs.getInt(6)));
                f.append(',');
                f.append(String.valueOf(rs.getInt(7)));
                f.append(',');
                f.append(String.valueOf(rs.getBigDecimal(8)));
                f.append(',');
                f.append(String.valueOf(rs.getInt(9)));
                f.append(',');
                f.append(String.valueOf(rs.getBigDecimal(10)));
                f.append(',');
                f.append(rs.getString(11));
                f.append(',');
                String aux = rs.getString(12).replace(',','/');
                f.append(aux);
                f.append(',');
                f.append(String.valueOf(rs.getTimestamp(13)));
                f.append('\n');
            }
            f.flush();
            f.close();

            //Tabela film_actor
            filename = "TabelasCSV/film_actor.csv";
            f = new FileWriter(filename);
            query = "select * from film_actor";
            st = con.createStatement();
            rs = st.executeQuery(query);
            f.append("actor_id,film_id,last_update");
            f.append('\n');

            while(rs.next()){
                f.append(String.valueOf(rs.getInt(1)));
                f.append(',');
                f.append(String.valueOf(rs.getInt(2)));
                f.append(',');
                f.append(String.valueOf(rs.getTimestamp(3)));
                f.append('\n');
            }
            f.flush();
            f.close();

            //Tabela film_category
            filename = "TabelasCSV/film_category.csv";
            f = new FileWriter(filename);
            query = "select * from film_category";
            st = con.createStatement();
            rs = st.executeQuery(query);
            f.append("film_id,category_id,last_update");
            f.append('\n');

            while(rs.next()){
                f.append(String.valueOf(rs.getInt(1)));
                f.append(',');
                f.append(String.valueOf(rs.getInt(2)));
                f.append(',');
                f.append(String.valueOf(rs.getTimestamp(3)));
                f.append('\n');
            }
            f.flush();
            f.close();

            //Tabela film_text -- n sei se é preciso exportar esta, parece mais uma view do que uma tabela mesmo
            filename = "TabelasCSV/film_text.csv";
            f = new FileWriter(filename);
            query = "select * from film_text";
            st = con.createStatement();
            rs = st.executeQuery(query);
            f.append("film_id,title,description");
            f.append('\n');

            while(rs.next()){
                f.append(String.valueOf(rs.getInt(1)));
                f.append(',');
                f.append(rs.getString(2));
                f.append(',');
                f.append(rs.getString(3));
                f.append('\n');
            }
            f.flush();
            f.close();

            //Tabela language
            filename = "TabelasCSV/language.csv";
            f = new FileWriter(filename);
            query = "select * from language";
            st = con.createStatement();
            rs = st.executeQuery(query);
            f.append("language_id,name,last_update");
            f.append('\n');

            while(rs.next()){
                f.append(String.valueOf(rs.getInt(1)));
                f.append(',');
                f.append(rs.getString(2));
                f.append(',');
                f.append(String.valueOf(rs.getTimestamp(3)));
                f.append('\n');
            }
            f.flush();
            f.close();

            //Tabela inventory
            filename = "TabelasCSV/inventory.csv";
            f = new FileWriter(filename);
            query = "select * from inventory";
            st = con.createStatement();
            rs = st.executeQuery(query);
            f.append("inventory_id,film_id,store_id,last_update");
            f.append('\n');

            while(rs.next()){
                f.append(String.valueOf(rs.getInt(1)));
                f.append(',');
                f.append(String.valueOf(rs.getInt(2)));
                f.append(',');
                f.append(String.valueOf(rs.getInt(3)));
                f.append(',');
                f.append(String.valueOf(rs.getTimestamp(4)));
                f.append('\n');
            }
            f.flush();
            f.close();

            //Tabela payment
            filename = "TabelasCSV/payment.csv";
            f = new FileWriter(filename);
            query = "select * from payment";
            st = con.createStatement();
            rs = st.executeQuery(query);
            f.append("payment_id,customer_id,staff_id,rental_id,amount,payment_date,last_update");
            f.append('\n');

            while(rs.next()){
                f.append(String.valueOf(rs.getInt(1)));
                f.append(',');
                f.append(String.valueOf(rs.getInt(2)));
                f.append(',');
                f.append(String.valueOf(rs.getInt(3)));
                f.append(',');
                f.append(String.valueOf(rs.getInt(4)));
                f.append(',');
                f.append(String.valueOf(rs.getBigDecimal(5)));
                f.append(',');
                f.append(String.valueOf(rs.getDate(6)));
                f.append(' ' + String.valueOf(rs.getTime(6)));
                f.append(',');
                f.append(String.valueOf(rs.getTimestamp(7)));
                f.append('\n');
            }
            f.flush();
            f.close();

            //Tabela rental
            filename = "TabelasCSV/rental.csv";
            f = new FileWriter(filename);
            query = "select * from rental";
            st = con.createStatement();
            rs = st.executeQuery(query);
            f.append("rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update");
            f.append('\n');

            while(rs.next()){
                f.append(String.valueOf(rs.getInt(1)));
                f.append(',');
                f.append(String.valueOf(rs.getDate(2)));
                f.append(' ' + String.valueOf(rs.getTime(2)));
                f.append(',');
                f.append(String.valueOf(rs.getInt(3)));
                f.append(',');
                f.append(String.valueOf(rs.getInt(4)));
                f.append(',');
                f.append(String.valueOf(rs.getDate(5)));
                f.append(' ' + String.valueOf(rs.getTime(5)));
                f.append(',');
                f.append(String.valueOf(rs.getInt(6)));
                f.append(',');
                f.append(String.valueOf(rs.getTimestamp(7)));
                f.append('\n');
            }
            f.flush();
            f.close();

            //Tabela staff
            filename = "TabelasCSV/staff.csv";
            f = new FileWriter(filename);
            query = "select * from staff";
            st = con.createStatement();
            rs = st.executeQuery(query);
            f.append("staff_id,first_name,last_name,address_id,picture,email,store_id,active,username,password,last_update");
            f.append('\n');

            while(rs.next()){
                f.append(String.valueOf(rs.getInt(1)));
                f.append(',');
                f.append(rs.getString(2));
                f.append(',');
                f.append(rs.getString(3));
                f.append(',');
                f.append(String.valueOf(rs.getInt(4)));
                f.append(',');
                f.append(String.valueOf(rs.getBlob(5)));
                f.append(',');
                f.append(rs.getString(6));
                f.append(',');
                f.append(String.valueOf(rs.getInt(7)));
                f.append(',');
                f.append(String.valueOf(rs.getBoolean(8)));
                f.append(',');
                f.append(rs.getString(9));
                f.append(',');
                f.append(rs.getString(10));
                f.append(',');
                f.append(String.valueOf(rs.getTimestamp(11)));
                f.append('\n');
            }
            f.flush();
            f.close();

            //Tabela store
            filename = "TabelasCSV/store.csv";
            f = new FileWriter(filename);
            query = "select * from store";
            st = con.createStatement();
            rs = st.executeQuery(query);
            f.append("store_id,manager_staff_id,address_id,last_update");
            f.append('\n');

            while(rs.next()){
                f.append(String.valueOf(rs.getInt(1)));
                f.append(',');
                f.append(String.valueOf(rs.getInt(2)));
                f.append(',');
                f.append(String.valueOf(rs.getInt(3)));
                f.append(',');
                f.append(String.valueOf(rs.getTimestamp(4)));
                f.append('\n');
            }
            f.flush();
            f.close();

        } catch (Exception e){
            e.printStackTrace();
        }
    }
}